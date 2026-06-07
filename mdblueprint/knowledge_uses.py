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

def _declaration_graph(idx: LeanIndex) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
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


def _node_declaration_map(nodes: list[Node]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for node in nodes:
        if node.lean is None:
            continue
        mapping[node.id] = list(node.lean.declarations)
    return mapping


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
) -> list[InferredUse]:
    """Infer Lean-backed ``uses`` edges for one node.

    The inference is intentionally conservative. It only emits edges when a
    target node is supported by an explicit markdown node reference or by a
    declaration reachable from the source node's Lean declarations.
    """
    nodes_by_id = {candidate.id: candidate for candidate in all_nodes}
    decls_by_node = _node_declaration_map(all_nodes)
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
        decl_graph = _declaration_graph(idx)
        reachable = _reachable_decls(source_decls, decl_graph, max_depth=max_depth)
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


def inferred_uses(node: Node, all_nodes: list[Node], idx: LeanIndex, *, max_depth: int = 3) -> list[str]:
    return [item.target_node_id for item in infer_uses_for_node(node, all_nodes, idx, max_depth=max_depth)]

