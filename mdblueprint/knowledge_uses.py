"""Infer conservative ``uses`` edges from Lean and node-local evidence."""
from __future__ import annotations

import re
from dataclasses import dataclass

from tools.knowledge.lean_index import LeanDeclaration, LeanIndex
from tools.knowledge.models import Node
from tools.knowledge.node_refs import NODE_REF_RE, THEOREM_KINDS, _split_body_proof, _strip_see_also_sections


@dataclass(frozen=True)
class InferredUse:
    source_node_id: str
    target_node_id: str
    evidence: str
    via: tuple[str, ...] = ()


@dataclass(frozen=True)
class UsesInferenceContext:
    idx: LeanIndex
    nodes_by_id: dict[str, Node]
    decls_by_node: dict[str, list[str]]
    reference_index: dict[str, list[str]]
    decl_graph: dict[str, list[str]]


def _unique_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def _strip_lean_comments(text: str) -> str:
    text = re.sub(r"/-.*?-/", " ", text, flags=re.S)
    return re.sub(r"--.*", " ", text)


def _decl_text(decl: LeanDeclaration, idx: LeanIndex) -> str:
    try:
        lines = decl.file.read_text(encoding="utf-8").splitlines()
    except OSError:
        return decl.signature or ""

    next_line = len(lines) + 1
    for other in idx.declarations.values():
        if other.file == decl.file and other.line > decl.line:
            next_line = min(next_line, other.line)

    start = max(decl.line - 1, 0)
    end = max(next_line - 1, start + 1)
    return _strip_lean_comments("\n".join(lines[start:end])).strip()


_COMMON_LEAN_LEAF_NAMES = frozenset({
    "allocation",
    "bind",
    "map",
    "mem",
    "one",
    "pure",
    "ret",
    "value",
    "winner",
})

_LEAN_NAME_RE = re.compile(r"[A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z][A-Za-z0-9_]*)*")


def _reference_index(declarations: dict[str, LeanDeclaration]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}
    for name, decl in declarations.items():
        index.setdefault(name, []).append(name)
        leaf = decl.qualified_name.rsplit(".", 1)[-1]
        if len(leaf) >= 4 and leaf not in _COMMON_LEAN_LEAF_NAMES:
            index.setdefault(leaf, []).append(name)
    return index


def _decl_references(text: str, reference_index: dict[str, list[str]]) -> list[str]:
    refs: list[str] = []
    for match in _LEAN_NAME_RE.finditer(text):
        token = match.group(0)
        for candidate in reference_index.get(token, []):
            refs.append(candidate)
        if "." in token:
            leaf = token.rsplit(".", 1)[-1]
            for candidate in reference_index.get(leaf, []):
                refs.append(candidate)
    return _unique_preserve_order(refs)


def _build_decl_graph(idx: LeanIndex, reference_index: dict[str, list[str]] | None = None) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    if reference_index is None:
        reference_index = _reference_index(idx.declarations)
    for name, decl in idx.declarations.items():
        text = _decl_text(decl, idx)
        refs = [
            ref
            for ref in _decl_references(text, reference_index)
            if ref != name
        ]
        graph[name] = refs
    return graph


def _build_node_decl_map(nodes: list[Node]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for node in nodes:
        if node.lean is None:
            continue
        mapping[node.id] = list(node.lean.declarations)
    return mapping


def build_uses_inference_context(nodes: list[Node], idx: LeanIndex) -> UsesInferenceContext:
    """Build the cached structures needed to infer and prune uses edges."""
    decls_by_node = _build_node_decl_map(nodes)
    reference_index = _reference_index(idx.declarations)
    return UsesInferenceContext(
        idx=idx,
        nodes_by_id={node.id: node for node in nodes},
        decls_by_node=decls_by_node,
        reference_index=reference_index,
        decl_graph=_build_decl_graph(idx, reference_index),
    )


def _reachable_decls(
    start: list[str],
    graph: dict[str, list[str]],
    *,
    max_depth: int,
) -> dict[str, tuple[str, ...]]:
    reachable: dict[str, tuple[str, ...]] = {}
    queue: list[tuple[str, tuple[str, ...], int]] = [
        (name, (name,), 0) for name in start if name in graph
    ]
    seen = set(start)

    while queue:
        current, path, depth = queue.pop(0)
        if depth >= max_depth:
            continue
        for ref in graph.get(current, []):
            if ref in seen:
                continue
            seen.add(ref)
            ref_path = (*path, ref)
            reachable[ref] = ref_path
            queue.append((ref, ref_path, depth + 1))
    return reachable


def _common_prefix_len(left: str, right: str) -> int:
    count = 0
    for a, b in zip(left.split("."), right.split(".")):
        if a != b:
            break
        count += 1
    return count


def _compatible_dependency(source_id: str, target_id: str) -> bool:
    source_root = source_id.split(".", 1)[0]
    target_root = target_id.split(".", 1)[0]
    if source_root == target_root:
        if source_root == "social_choice":
            return _common_prefix_len(source_id, target_id) >= 3
        if source_root == "game_theory":
            return _common_prefix_len(source_id, target_id) >= 2
        return True
    if target_root == "math":
        return True
    if source_root == "math" and target_root in {"game_theory", "social_choice", "mechanism_design"}:
        return True
    return False


def infer_uses_for_node(
    node: Node,
    all_nodes: list[Node],
    idx: LeanIndex,
    *,
    max_depth: int = 3,
    include_body_refs: bool = True,
    context: UsesInferenceContext | None = None,
) -> list[InferredUse]:
    """Infer Lean-backed ``uses`` edges for one node.

    The inference is intentionally conservative. It only emits edges when a
    target node is supported by an explicit markdown node reference or by a
    declaration reachable from the source node's Lean declarations.
    """
    if context is None:
        context = build_uses_inference_context(all_nodes, idx)

    nodes_by_id = context.nodes_by_id
    decls_by_node = context.decls_by_node
    source_decls = [
        name
        for name in decls_by_node.get(node.id, [])
        if name in idx.declarations
    ]

    inferred: list[InferredUse] = []
    if include_body_refs and node.kind in THEOREM_KINDS:
        _, proof_text = _split_body_proof(node.body or "")
        if proof_text:
            proof_text = _strip_see_also_sections(proof_text)
            for match in NODE_REF_RE.finditer(proof_text):
                target = match.group(1)
                if target != node.id and target in nodes_by_id:
                    inferred.append(InferredUse(node.id, target, "body_node_ref", (target,)))

    if source_decls:
        reachable = _reachable_decls(source_decls, context.decl_graph, max_depth=max_depth)
        mapped_decls = {
            decl_name
            for mapped_node_id, decl_names in decls_by_node.items()
            if mapped_node_id != node.id
            for decl_name in decl_names
        }
        for target_id, target_decls in decls_by_node.items():
            if target_id == node.id:
                continue
            if not _compatible_dependency(node.id, target_id):
                continue
            for target_decl in target_decls:
                if target_decl not in reachable:
                    continue
                path = reachable[target_decl]
                intermediates = path[1:-1]
                if intermediates and any(intermediate in mapped_decls for intermediate in intermediates):
                    continue
                inferred.append(
                    InferredUse(
                        node.id,
                        target_id,
                        "lean_transitive_decl" if intermediates else "lean_direct_decl",
                        path,
                    )
                )
                break

    deduped: dict[str, InferredUse] = {}
    for item in inferred:
        deduped.setdefault(item.target_node_id, item)
    return [deduped[target] for target in sorted(deduped)]


def _path_exists_excluding_direct(
    edges: dict[str, list[str]],
    *,
    start: str,
    goal: str,
    excluded_first_hop: str,
) -> bool:
    seen: set[str] = {start}
    queue: list[str] = []
    for neighbor in edges.get(start, []):
        if neighbor == excluded_first_hop:
            continue
        if neighbor == goal:
            return True
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append(neighbor)
    while queue:
        current = queue.pop(0)
        for neighbor in edges.get(current, []):
            if neighbor == goal:
                return True
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return False


def _find_cycle(edges: dict[str, list[str]]) -> list[str] | None:
    """Return one directed cycle from the graph, or ``None`` if acyclic."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color: dict[str, int] = {nid: WHITE for nid in edges}
    parent: dict[str, str | None] = {nid: None for nid in edges}

    def dfs(u: str) -> list[str] | None:
        color[u] = GRAY
        for v in edges.get(u, []):
            if v not in color:
                continue
            if color[v] == GRAY:
                cycle = [v, u]
                p = parent.get(u)
                while p is not None and p != v:
                    cycle.append(p)
                    p = parent.get(p)
                cycle.reverse()
                return cycle
            if color[v] == WHITE:
                parent[v] = u
                result = dfs(v)
                if result is not None:
                    return result
        color[u] = BLACK
        return None

    for nid in sorted(edges):
        if color[nid] == WHITE:
            cycle = dfs(nid)
            if cycle is not None:
                return cycle
    return None


def _edge_removal_priority(item: InferredUse) -> tuple[int, int, str, str]:
    """Rank edges from weakest to strongest for deterministic cycle breaking."""
    evidence_rank = {
        "body_node_ref": 0,
        "lean_transitive_decl": 1,
        "lean_direct_decl": 2,
    }.get(item.evidence, 1)
    # Prefer removing longer transitive chains before direct edges.
    return (evidence_rank, -len(item.via), item.source_node_id, item.target_node_id)


def prune_redundant_inferred_uses(
    uses_by_node: dict[str, list[InferredUse]],
) -> dict[str, list[InferredUse]]:
    """Remove transitive duplicate edges from a proposed uses graph.

    The input is the proposed dependency set after evidence collection.
    Any edge that is already implied by another path in the proposed graph is
    dropped. If cycles still remain, the weakest edge in each cycle is removed
    until the result is acyclic. This leaves a minimal DAG-style dependency
    layer suitable for graph validation.
    """
    edges: dict[str, list[str]] = {
        node_id: _unique_preserve_order([
            item.target_node_id
            for item in items
            if item.evidence != "body_node_ref"
        ])
        for node_id, items in uses_by_node.items()
    }

    changed = True
    while changed:
        changed = False
        for node_id in sorted(edges):
            direct = list(edges.get(node_id, []))
            if len(direct) < 2:
                continue
            pruned = []
            for dep in direct:
                if _path_exists_excluding_direct(edges, start=node_id, goal=dep, excluded_first_hop=dep):
                    changed = True
                    continue
                pruned.append(dep)
            edges[node_id] = pruned

    while True:
        cycle = _find_cycle(edges)
        if cycle is None:
            break
        cycle_edges = list(zip(cycle, cycle[1:] + cycle[:1]))
        removable: list[InferredUse] = []
        for source, target in cycle_edges:
            for item in uses_by_node.get(source, []):
                if item.target_node_id == target:
                    removable.append(item)
                    break
        if not removable:
            break
        weakest = min(removable, key=_edge_removal_priority)
        edges[weakest.source_node_id] = [
            dep for dep in edges.get(weakest.source_node_id, [])
            if dep != weakest.target_node_id
        ]

    result: dict[str, list[InferredUse]] = {}
    for node_id, items in uses_by_node.items():
        keep = set(edges.get(node_id, []))
        result[node_id] = [
            item for item in items
            if item.evidence != "body_node_ref" and item.target_node_id in keep
        ]
    return result


def infer_and_prune_uses_for_nodes(
    nodes: list[Node],
    idx: LeanIndex,
    *,
    max_depth: int = 3,
    include_body_refs: bool = True,
) -> dict[str, list[InferredUse]]:
    """Infer uses for every node, then prune transitive duplicates and cycles."""
    context = build_uses_inference_context(nodes, idx)
    proposed: dict[str, list[InferredUse]] = {}
    for node in nodes:
        proposed[node.id] = infer_uses_for_node(
            node,
            nodes,
            idx,
            max_depth=max_depth,
            include_body_refs=include_body_refs,
            context=context,
        )
    return prune_redundant_inferred_uses(proposed)


def inferred_uses(node: Node, all_nodes: list[Node], idx: LeanIndex, *, max_depth: int = 3) -> list[str]:
    return [item.target_node_id for item in infer_uses_for_node(node, all_nodes, idx, max_depth=max_depth)]
