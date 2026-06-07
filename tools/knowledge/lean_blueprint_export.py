"""Export a Lean-backed knowledge tree into a self-contained mdblueprint repo."""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from dataclasses import dataclass, replace
from pathlib import Path

import yaml

from mdblueprint.knowledge_uses import infer_and_prune_uses_for_nodes
from mdblueprint.knowledge_generation import _render_node
from mdblueprint.knowledge_verification import KnowledgeVerificationResult, verify_knowledge_tree
from tools.knowledge.config import (
    DEFAULT_CONFIG_NAME,
    GraphDisplayConfig,
    LeanConfig,
    LeanRepositoryConfig,
    LintConfig,
    MathConfig,
    ProjectConfig,
    SiteConfig,
    SourcesConfig,
    TopicConfig,
    load_project_config,
)
from tools.knowledge.lean_index import index_lean_project
from tools.knowledge.models import Node
from tools.knowledge.parser import parse_file


DEFAULT_SOURCE_URL_TEMPLATE = "{web_url}/blob/{revision}/{path}#L{line}"


@dataclass(frozen=True)
class BlueprintExportResult:
    source_root: Path
    lean_root: Path
    output_root: Path
    config_path: Path
    node_count: int
    topic_count: int
    final_edge_count: int
    node_paths: tuple[Path, ...]
    config_generated: bool
    verification: KnowledgeVerificationResult | None = None
    warnings: tuple[str, ...] = ()


def _git_origin(path: Path) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(path), "remote", "get-url", "origin"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
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


def _titleize(text: str) -> str:
    return text.replace("_", " ").replace("-", " ").title()


def _topic_title(topic_id: str) -> str:
    return _titleize(topic_id)


def _unique_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def _node_topic_ids(node: Node, source_root: Path) -> list[str]:
    topic_ids: list[str] = []
    if node.primary_topic:
        topic_ids.append(node.primary_topic)
    topic_ids.extend(node.topics)
    if node.file_path is not None:
        try:
            rel = node.file_path.relative_to(source_root)
        except ValueError:
            rel = None
        if rel is not None and rel.parts and rel.parts[0] in {"nodes", "staged"}:
            stem_parts = list(rel.with_suffix("").parts[1:-1])
            for size in range(1, len(stem_parts) + 1):
                topic_ids.append(".".join(stem_parts[:size]))
    return _unique_preserve_order([topic for topic in topic_ids if topic])


def _collect_topic_entries(nodes: list[Node], source_root: Path, source_config: ProjectConfig | None) -> list[dict[str, object]]:
    topic_lookup: dict[str, TopicConfig] = {}
    ordered_ids: list[str] = []

    if source_config is not None:
        for topic in source_config.topics:
            topic_lookup[topic.id] = topic
            ordered_ids.append(topic.id)

    for node in nodes:
        for topic_id in _node_topic_ids(node, source_root):
            if topic_id not in topic_lookup and topic_id not in ordered_ids:
                ordered_ids.append(topic_id)

    entries: list[dict[str, object]] = []
    for topic_id in ordered_ids:
        topic = topic_lookup.get(topic_id)
        if topic is not None:
            payload: dict[str, object] = {
                "id": topic.id,
                "title": topic.title,
            }
            if topic.aliases:
                payload["aliases"] = list(topic.aliases)
            entries.append(payload)
        else:
            entries.append({"id": topic_id, "title": _topic_title(topic_id)})
    return entries


def _path_value(path: Path, config_dir: Path) -> str:
    try:
        return os.path.relpath(path, config_dir)
    except ValueError:
        return str(path)


def _build_lean_payload(lean_root: Path, output_root: Path, source_config: ProjectConfig | None) -> dict[str, object] | None:
    repos: list[dict[str, object]] = []
    default_repository: str | None = None

    if source_config is not None and source_config.lean.repositories:
        for repo in source_config.lean.repositories.values():
            repo_payload: dict[str, object] = {
                "id": repo.id,
                "title": repo.title,
                "local_path": _path_value(repo.local_path, output_root),
                "web_url": repo.web_url,
                "source_url_template": repo.source_url_template,
                "revision": repo.revision,
            }
            if repo.subdir:
                repo_payload["subdir"] = repo.subdir
            if repo.doc_url_template:
                repo_payload["doc_url_template"] = repo.doc_url_template
            repos.append(repo_payload)
        default_repository = source_config.lean.default_repository
        if default_repository is None and len(repos) == 1:
            default_repository = repos[0]["id"]
    else:
        origin = _git_origin(lean_root)
        web_url = _repo_origin_to_web_url(origin) if origin else None
        if web_url is None:
            return None
        repos.append({
            "id": "default",
            "title": _titleize(lean_root.name),
            "local_path": _path_value(lean_root, output_root),
            "web_url": web_url,
            "source_url_template": DEFAULT_SOURCE_URL_TEMPLATE,
            "revision": _git_rev_parse(lean_root) or "auto",
        })
        default_repository = "default"

    if not repos:
        return None

    payload: dict[str, object] = {"repositories": repos}
    if default_repository is not None:
        payload["default_repository"] = default_repository
    return payload


def _math_payload(math: MathConfig) -> dict[str, object]:
    return {
        "macros": dict(math.macros),
        "delimiters": {
            "inline": [list(item) for item in math.inline_delimiters],
            "display": [list(item) for item in math.display_delimiters],
        },
        "throw_on_error": math.throw_on_error,
    }


def _graph_payload(graph: GraphDisplayConfig) -> dict[str, object]:
    return {
        "max_visible_nodes": graph.max_visible_nodes,
        "max_expand_nodes": graph.max_expand_nodes,
        "proof_plans": graph.proof_plans,
        "max_page_total": graph.max_page_total,
        "inline_child_max_size": graph.inline_child_max_size,
    }


def _sources_payload(sources: SourcesConfig) -> dict[str, object]:
    library = []
    for entry in sources.library.values():
        payload: dict[str, object] = {
            "id": entry.id,
            "title": entry.title,
        }
        if entry.short is not None:
            payload["short"] = entry.short
        if entry.authors is not None:
            payload["authors"] = entry.authors
        if entry.path is not None:
            payload["path"] = entry.path
        library.append(payload)
    return {
        "library": library,
        "require_source_spans": sources.require_source_spans,
    }


def _lint_payload(lint: LintConfig) -> dict[str, object]:
    return {
        "fuzzy_threshold": lint.fuzzy_threshold,
        "semantic_candidate_threshold": lint.semantic_candidate_threshold,
        "plan_promote_severity": lint.plan_promote_severity,
        "hierarchy_inversion_severity": lint.hierarchy_inversion_severity,
        "topic_lean_aliases": dict(lint.topic_lean_aliases),
    }


def _write_yaml(path: Path, payload: dict[str, object]) -> None:
    path.write_text(
        yaml.safe_dump(payload, sort_keys=False, allow_unicode=True).rstrip() + "\n",
        encoding="utf-8",
    )


def _load_source_config(source_root: Path) -> ProjectConfig | None:
    config_path = source_root / DEFAULT_CONFIG_NAME
    if not config_path.exists():
        return None
    return load_project_config(source_root)


def _source_node_paths(source_root: Path) -> list[Path]:
    paths: list[Path] = []
    for base in (source_root / "nodes", source_root / "staged"):
        if base.is_dir():
            for path in sorted(base.rglob("*.md")):
                if path.name != "topics.md":
                    paths.append(path)
    return paths


def _load_nodes(source_root: Path) -> list[Node]:
    return [parse_file(path) for path in _source_node_paths(source_root)]


def _write_node(path: Path, node: Node) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_render_node(node), encoding="utf-8")


def _write_config(
    *,
    source_root: Path,
    output_root: Path,
    lean_root: Path,
    nodes: list[Node],
    source_config: ProjectConfig | None,
) -> Path:
    payload: dict[str, object] = {}

    site_title = source_config.site.title if source_config is not None else _titleize(lean_root.name)
    payload["site"] = {"title": site_title}
    if source_config is not None and source_config.site.short_title is not None:
        payload["site"]["short_title"] = source_config.site.short_title

    topic_entries = _collect_topic_entries(nodes, source_root, source_config)
    if topic_entries:
        payload["topics"] = topic_entries

    if source_config is not None:
        payload["math"] = _math_payload(source_config.math)
        payload["graph"] = _graph_payload(source_config.graph)
        payload["sources"] = _sources_payload(source_config.sources)
        payload["lint"] = _lint_payload(source_config.lint)

    lean_payload = _build_lean_payload(lean_root, output_root, source_config)
    if lean_payload is not None:
        payload["lean"] = lean_payload

    config_path = output_root / DEFAULT_CONFIG_NAME
    _write_yaml(config_path, payload)
    return config_path


def export_blueprint_tree(
    lean_root: Path,
    source_root: Path,
    output_root: Path,
    *,
    verify_against: Path | None = None,
) -> BlueprintExportResult:
    lean_root = lean_root.resolve()
    source_root = source_root.resolve()
    output_root = output_root.resolve()
    if source_root == output_root:
        raise ValueError("source_root and output_root must be different directories")

    source_config = _load_source_config(source_root)
    if output_root.exists():
        shutil.rmtree(output_root)
    shutil.copytree(source_root, output_root)

    nodes = _load_nodes(source_root)
    idx = index_lean_project(lean_root)
    uses_map = infer_and_prune_uses_for_nodes(nodes, idx)
    node_paths: list[Path] = []
    final_edge_count = 0
    for node in nodes:
        final_uses = [item.target_node_id for item in uses_map.get(node.id, [])]
        final_edge_count += len(final_uses)
        updated = replace(node, uses=final_uses)
        if node.file_path is None:
            continue
        try:
            rel = node.file_path.relative_to(source_root)
        except ValueError:
            rel = node.file_path.name
        out_path = output_root / rel
        _write_node(out_path, updated)
        node_paths.append(out_path)

    config_path = _write_config(
        source_root=source_root,
        output_root=output_root,
        lean_root=lean_root,
        nodes=nodes,
        source_config=source_config,
    )

    verification = None
    if verify_against is not None:
        verification = verify_knowledge_tree(verify_against, output_root)

    return BlueprintExportResult(
        source_root=source_root,
        lean_root=lean_root,
        output_root=output_root,
        config_path=config_path,
        node_count=len(nodes),
        topic_count=len(_collect_topic_entries(nodes, source_root, source_config)),
        final_edge_count=final_edge_count,
        node_paths=tuple(sorted(node_paths)),
        config_generated=source_config is None,
        verification=verification,
        warnings=tuple(idx.warnings),
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export a Lean-backed docs/knowledge tree with inferred uses and a generated mdblueprint.yml",
    )
    parser.add_argument("lean_root", type=Path)
    parser.add_argument("source_root", type=Path, help="Input docs/knowledge-style tree to export")
    parser.add_argument("output_root", type=Path)
    parser.add_argument("--verify-against", type=Path, default=None, help="Optional reference tree to compare against after export")
    args = parser.parse_args()

    result = export_blueprint_tree(
        args.lean_root,
        args.source_root,
        args.output_root,
        verify_against=args.verify_against,
    )
    print(f"exported {result.node_count} nodes, {result.topic_count} topics, {result.final_edge_count} uses edges into {result.output_root}")
    print(f"config: {result.config_path}")
    if result.verification is not None:
        print("verification:", "clean" if result.verification.clean else "dirty")
        for diff in result.verification.diffs:
            print(diff)
    for warning in result.warnings:
        print("warning:", warning)


if __name__ == "__main__":
    main()
