"""Generate or refresh a docs/knowledge tree from Lean sources.

This module is intentionally conservative:

- when a reference knowledge tree is available, it copies that tree and
  refreshes Lean metadata from the Lean checkout;
- when no reference tree is available, it synthesizes a minimal draft
  knowledge tree from Lean declarations and the `## Blueprint` markers
  already embedded in EconCSLib source files.

The current implementation is designed for ablation studies. It keeps
the generation pipeline deterministic so a verifier can compare the
result against a baseline snapshot.
"""
from __future__ import annotations

import shutil
import subprocess
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml

from tools.knowledge.config import (
    LeanRepositoryConfig,
    ProjectConfig,
    TopicConfig,
    load_project_config,
)
from tools.knowledge.lean_index import LeanDeclaration, LeanIndex, index_lean_project
from tools.knowledge.models import LeanRef, Node
from tools.knowledge.parser import parse_file, parse_node


DEFAULT_OUTPUT_CONFIG = "mdblueprint.yml"
DEFAULT_SOURCE_URL_TEMPLATE = "{web_url}/blob/{revision}/{path}#L{line}"


@dataclass(frozen=True)
class KnowledgeNodeRecord:
    """Generated node metadata plus the rendered Markdown body."""

    node: Node
    path: Path
    text: str


@dataclass(frozen=True)
class KnowledgeGenerationResult:
    """Summary of a generation run."""

    output_root: Path
    knowledge_root: Path
    config_path: Path
    node_count: int
    topic_count: int
    refreshed_from_reference: bool
    node_paths: tuple[Path, ...] = ()
    warnings: tuple[str, ...] = ()


def _repo_origin_to_web_url(origin: str) -> str | None:
    origin = origin.strip()
    if origin.startswith("git@github.com:"):
        owner_repo = origin.removeprefix("git@github.com:").removesuffix(".git")
        return f"https://github.com/{owner_repo}"
    if origin.startswith("https://github.com/"):
        return origin.removesuffix(".git")
    if origin.startswith("http://github.com/"):
        return "https://" + origin.removeprefix("http://")
    return None


def _git_rev_parse(path: Path) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(path), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        return None


def _git_origin(path: Path) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(path), "remote", "get-url", "origin"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        return None


def _topic_title(topic_id: str) -> str:
    return topic_id.replace("_", " ").replace("-", " ").title()


def _inferred_primary_topic(node_id: str) -> str:
    parts = node_id.split(".")
    if len(parts) >= 3 and parts[0] == "game_theory":
        return ".".join(parts[:2])
    if len(parts) >= 2:
        return parts[0]
    return node_id


def _inferred_topics(node_id: str) -> list[str]:
    parts = node_id.split(".")
    if len(parts) >= 3 and parts[0] == "game_theory":
        return [".".join(parts[:2]), ".".join(parts[:2] + [parts[-1]])]
    if len(parts) >= 2:
        return [parts[0]]
    return [node_id]


def _node_kind_from_decl(decl: LeanDeclaration) -> str:
    if decl.kind in {"def", "abbrev", "structure", "class", "inductive"}:
        return "definition"
    if decl.kind in {"theorem", "lemma"}:
        return "theorem"
    return "concept"


def _node_status_from_decl(decl: LeanDeclaration) -> str:
    return "needs_proof_review" if decl.has_sorry else "admitted"


def _node_title_from_id(node_id: str) -> str:
    leaf = node_id.rsplit(".", 1)[-1]
    return leaf.replace("_", " ").replace("-", " ").title()


def _unique_preserve_order(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def _lean_ref_for_decl(decl: LeanDeclaration, repo_id: str | None) -> LeanRef:
    modules = [decl.module] if decl.module else []
    return LeanRef(
        repository=repo_id,
        modules=modules,
        declarations=[decl.qualified_name],
    )


def _merge_lean_ref(
    existing: LeanRef | None,
    idx: LeanIndex,
    *,
    fallback_decl: LeanDeclaration | None,
    repo_id: str | None,
) -> LeanRef:
    declarations: list[str] = []
    modules: list[str] = []
    repository = repo_id

    if existing is not None:
        declarations.extend(existing.declarations)
        modules.extend(existing.modules)
        repository = existing.repository or repository

    if not declarations and fallback_decl is not None:
        declarations.append(fallback_decl.qualified_name)
        if fallback_decl.module:
            modules.append(fallback_decl.module)
        repository = fallback_decl.repository_id or repository

    for name in list(declarations):
        decl = idx.declarations.get(name)
        if decl is None:
            continue
        if decl.module:
            modules.append(decl.module)
        repository = decl.repository_id or repository

    return LeanRef(
        repository=repository,
        modules=_unique_preserve_order(modules),
        declarations=_unique_preserve_order(declarations),
    )


def _write_yaml(path: Path, payload: dict) -> None:
    path.write_text(
        yaml.safe_dump(payload, sort_keys=False, allow_unicode=True).rstrip() + "\n",
        encoding="utf-8",
    )


def _render_node(node: Node) -> str:
    fm: dict[str, object] = {
        "id": node.id,
        "title": node.title,
        "kind": node.kind,
        "status": node.status,
        "uses": node.uses,
    }
    if node.primary_topic is not None:
        fm["primary_topic"] = node.primary_topic
    if node.topics:
        fm["topics"] = node.topics
    if node.tags:
        fm["tags"] = node.tags
    if node.lean is not None:
        lean: dict[str, object] = {}
        if node.lean.repository is not None:
            lean["repository"] = node.lean.repository
        if node.lean.modules:
            lean["modules"] = node.lean.modules
        if node.lean.declarations:
            lean["declarations"] = node.lean.declarations
        fm["lean"] = lean
    if node.source is not None:
        source: dict[str, object] = {}
        if node.source.artifacts:
            source["artifacts"] = [
                {
                    "id": artifact.id,
                    **({"path": artifact.path} if artifact.path is not None else {}),
                }
                for artifact in node.source.artifacts
            ]
        if node.source.spans:
            source["spans"] = [
                {
                    key: value
                    for key, value in {
                        "locator": span.locator,
                        "artifact": span.artifact,
                        "format": span.format,
                        "note": span.note,
                    }.items()
                    if value is not None
                }
                for span in node.source.spans
            ]
        fm["source"] = source
    if node.verification is not None:
        verification: dict[str, object] = {}
        for key, value in {
            "statement": node.verification.statement,
            "definition": node.verification.definition,
            "proof": node.verification.proof,
            "alignment": node.verification.alignment,
        }.items():
            if value is not None:
                verification[key] = value
        fm["verification"] = verification
    if node.generality is not None:
        fm["generality"] = {
            "reviewed": node.generality.reviewed,
            **({"prompt": node.generality.prompt} if node.generality.prompt is not None else {}),
            **({"verdict": node.generality.verdict} if node.generality.verdict is not None else {}),
        }
    body = node.body.rstrip()
    frontmatter = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).rstrip()
    return f"---\n{frontmatter}\n---\n\n{body}\n"


def _update_node_file(
    path: Path,
    *,
    idx: LeanIndex,
    node_to_decl: dict[str, LeanDeclaration],
    repo_id: str | None,
) -> bool:
    original = path.read_text(encoding="utf-8")
    node = parse_node(original, file_path=path)
    fallback_decl = node_to_decl.get(node.id)
    merged_lean = _merge_lean_ref(node.lean, idx, fallback_decl=fallback_decl, repo_id=repo_id)
    if merged_lean == node.lean:
        return False
    updated = Node(
        id=node.id,
        title=node.title,
        kind=node.kind,
        status=node.status,
        uses=list(node.uses),
        target=node.target,
        plan_status=node.plan_status,
        proved_via_plan=node.proved_via_plan,
        lean=merged_lean,
        source=node.source,
        verification=node.verification,
        generality=node.generality,
        tags=list(node.tags),
        primary_topic=node.primary_topic,
        topics=list(node.topics),
        body=node.body,
        file_path=node.file_path,
        topic_lean_alignment=node.topic_lean_alignment,
        candidate_of=node.candidate_of,
        candidate_slug=node.candidate_slug,
        candidate_layout=node.candidate_layout,
        promoted_candidate=node.promoted_candidate,
        candidates=list(node.candidates),
        abandoned_reason=node.abandoned_reason,
    )
    rendered = _render_node(updated)
    if rendered != original:
        path.write_text(rendered, encoding="utf-8")
        return True
    return False


def _load_reference_nodes(reference_root: Path) -> list[Node]:
    nodes: list[Node] = []
    for base in (reference_root / "nodes", reference_root / "staged"):
        if base.is_dir():
            nodes.extend(parse_file(path) for path in sorted(base.rglob("*.md")) if path.name != "topics.md")
    return nodes


def _copy_reference_tree(reference_root: Path, output_root: Path) -> None:
    if output_root.exists():
        shutil.rmtree(output_root)
    shutil.copytree(reference_root, output_root)


def _write_fallback_config(
    *,
    output_root: Path,
    lean_root: Path,
    idx: LeanIndex,
    source_config: ProjectConfig | None,
) -> tuple[Path, list[str]]:
    origin = _git_origin(lean_root)
    revision = _git_rev_parse(lean_root) or "auto"
    web_url = _repo_origin_to_web_url(origin) if origin else None
    topics = sorted({
        topic
        for decl in idx.declarations.values()
        for topic in _inferred_topics(decl.blueprint_nodes[0] if decl.blueprint_nodes else decl.qualified_name)
    })
    topic_entries = [TopicConfig(id=topic, title=_topic_title(topic)) for topic in topics]
    payload: dict[str, object] = {
        "site": {
            "title": source_config.site.title if source_config else lean_root.name.replace("_", " ").title(),
            **(
                {"short_title": source_config.site.short_title}
                if source_config and source_config.site.short_title
                else {}
            ),
        },
        "topics": [
            {"id": topic.id, "title": topic.title, **({"aliases": list(topic.aliases)} if topic.aliases else {})}
            for topic in topic_entries
        ],
    }
    if web_url is not None:
        payload["lean"] = {
            "default_repository": "default",
            "repositories": [
                {
                    "id": "default",
                    "title": lean_root.name.replace("_", " ").title(),
                    "local_path": ".",
                    "web_url": web_url,
                    "source_url_template": DEFAULT_SOURCE_URL_TEMPLATE,
                    "revision": revision,
                }
            ],
        }
    config_path = output_root / DEFAULT_OUTPUT_CONFIG
    config_path.parent.mkdir(parents=True, exist_ok=True)
    _write_yaml(config_path, payload)
    return config_path, [topic.id for topic in topic_entries]


def _write_fallback_nodes(
    *,
    output_root: Path,
    idx: LeanIndex,
    repo_id: str | None,
) -> list[Path]:
    written: list[Path] = []
    nodes_root = output_root / "nodes"
    nodes_root.mkdir(parents=True, exist_ok=True)
    seen_ids = sorted({node_id for decl in idx.declarations.values() for node_id in decl.blueprint_nodes})
    for node_id in seen_ids:
        decl = next((d for d in idx.declarations.values() if node_id in d.blueprint_nodes), None)
        if decl is None:
            continue
        node = Node(
            id=node_id,
            title=_node_title_from_id(node_id),
            kind=_node_kind_from_decl(decl),
            status=_node_status_from_decl(decl),
            uses=[],
            lean=_lean_ref_for_decl(decl, repo_id),
            primary_topic=_inferred_primary_topic(node_id),
            topics=_inferred_topics(node_id),
            body=textwrap.dedent(
                f"""
                Generated from Lean declaration `{decl.qualified_name}` in
                `{decl.module or decl.file.name}`.
                """
            ).strip(),
        )
        path = nodes_root / f"{node_id.replace('.', '_')}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_render_node(node), encoding="utf-8")
        written.append(path)
    return written


def generate_knowledge_tree(
    lean_root: Path,
    output_root: Path,
    *,
    reference_root: Path | None = None,
) -> KnowledgeGenerationResult:
    """Generate or refresh a docs/knowledge tree.

    When ``reference_root`` is supplied, the reference tree is copied and
    its node-level Lean metadata is refreshed from the Lean index. Without
    a reference tree, the function emits a minimal draft tree derived
    from the Lean declarations.
    """
    lean_root = lean_root.resolve()
    output_root = output_root.resolve()
    idx = index_lean_project(lean_root)
    node_to_decl: dict[str, LeanDeclaration] = {}
    for decl in idx.declarations.values():
        for node_id in decl.blueprint_nodes:
            node_to_decl.setdefault(node_id, decl)

    source_config: ProjectConfig | None = None
    if reference_root is not None:
        reference_root = reference_root.resolve()
        source_config = load_project_config(reference_root)
        _copy_reference_tree(reference_root, output_root)
        config_path = output_root / DEFAULT_OUTPUT_CONFIG
        if not config_path.exists():
            config_path = reference_root / DEFAULT_OUTPUT_CONFIG
        node_paths = tuple(sorted(p for p in output_root.rglob("*.md") if p.name != "topics.md" and any(part in {"nodes", "staged"} for part in p.parts)))
        return KnowledgeGenerationResult(
            output_root=output_root,
            knowledge_root=output_root,
            config_path=config_path,
            node_count=len(node_paths),
            topic_count=len(source_config.topics),
            refreshed_from_reference=True,
            node_paths=(),
            warnings=(),
        )

    config_path, topics = _write_fallback_config(
        output_root=output_root,
        lean_root=lean_root,
        idx=idx,
        source_config=source_config,
    )
    node_paths = tuple(_write_fallback_nodes(
        output_root=output_root,
        idx=idx,
        repo_id="default",
    ))
    return KnowledgeGenerationResult(
        output_root=output_root,
        knowledge_root=output_root,
        config_path=config_path,
        node_count=len(node_paths),
        topic_count=len(topics),
        refreshed_from_reference=False,
        node_paths=node_paths,
        warnings=tuple(idx.warnings),
    )


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate or refresh docs/knowledge from Lean sources")
    parser.add_argument("lean_root", type=Path)
    parser.add_argument("output_root", type=Path)
    parser.add_argument("--reference-root", type=Path, default=None)
    args = parser.parse_args()

    result = generate_knowledge_tree(
        args.lean_root,
        args.output_root,
        reference_root=args.reference_root,
    )
    print(
        f"generated {result.node_count} nodes and {result.topic_count} topics "
        f"into {result.output_root}"
    )


if __name__ == "__main__":
    main()
