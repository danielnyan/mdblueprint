"""Verify a generated docs/knowledge tree against a reference snapshot."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from tools.knowledge.parser import parse_file


@dataclass(frozen=True)
class KnowledgeVerificationResult:
    """Summary of a comparison between two knowledge trees."""

    reference_root: Path
    generated_root: Path
    config_matches: bool
    topic_catalog_matches: bool
    node_matches: bool
    diffs: tuple[str, ...] = ()

    @property
    def clean(self) -> bool:
        return self.config_matches and self.topic_catalog_matches and self.node_matches and not self.diffs


def _normalized_yaml(path: Path) -> object:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _collect_node_files(root: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for path in sorted(root.rglob("*.md")):
        if path.name == "topics.md":
            continue
        if "nodes" not in path.parts and "staged" not in path.parts:
            continue
        node = parse_file(path)
        out[node.id] = path
    return out


def _node_signature(path: Path) -> dict[str, object]:
    node = parse_file(path)
    return {
        "id": node.id,
        "title": node.title,
        "kind": node.kind,
        "status": node.status,
        "uses": node.uses,
        "primary_topic": node.primary_topic,
        "topics": node.topics,
        "lean": {
            "repository": node.lean.repository if node.lean else None,
            "modules": node.lean.modules if node.lean else [],
            "declarations": node.lean.declarations if node.lean else [],
        } if node.lean is not None else None,
        "source": {
            "artifacts": [
                {"id": artifact.id, "path": artifact.path}
                for artifact in node.source.artifacts
            ] if node.source is not None else [],
            "spans": [
                {
                    "locator": span.locator,
                    "artifact": span.artifact,
                    "format": span.format,
                    "note": span.note,
                }
                for span in node.source.spans
            ] if node.source is not None else [],
        } if node.source is not None else None,
        "verification": {
            "statement": node.verification.statement,
            "definition": node.verification.definition,
            "proof": node.verification.proof,
            "alignment": node.verification.alignment,
        } if node.verification is not None else None,
        "generality": {
            "reviewed": node.generality.reviewed,
            "prompt": node.generality.prompt,
            "verdict": node.generality.verdict,
        } if node.generality is not None else None,
        "tags": node.tags,
    }


def verify_knowledge_tree(
    reference_root: Path,
    generated_root: Path,
    *,
    compare_body: bool = False,
) -> KnowledgeVerificationResult:
    reference_root = reference_root.resolve()
    generated_root = generated_root.resolve()

    diffs: list[str] = []

    ref_config = _normalized_yaml(reference_root / "mdblueprint.yml")
    gen_config = _normalized_yaml(generated_root / "mdblueprint.yml")
    config_matches = ref_config == gen_config
    if not config_matches:
        diffs.append("mdblueprint.yml differs")

    ref_topics = {
        path.relative_to(reference_root).as_posix(): path.read_text(encoding="utf-8").strip()
        for path in reference_root.rglob("topics.md")
    }
    gen_topics = {
        path.relative_to(generated_root).as_posix(): path.read_text(encoding="utf-8").strip()
        for path in generated_root.rglob("topics.md")
    }
    topic_catalog_matches = ref_topics == gen_topics
    if not topic_catalog_matches:
        missing = sorted(set(ref_topics) - set(gen_topics))
        extra = sorted(set(gen_topics) - set(ref_topics))
        if missing:
            diffs.append(f"missing topic catalogs: {missing}")
        if extra:
            diffs.append(f"extra topic catalogs: {extra}")

    ref_nodes = _collect_node_files(reference_root)
    gen_nodes = _collect_node_files(generated_root)
    node_matches = True
    for node_id in sorted(set(ref_nodes) | set(gen_nodes)):
        ref_path = ref_nodes.get(node_id)
        gen_path = gen_nodes.get(node_id)
        if ref_path is None:
            node_matches = False
            diffs.append(f"extra node {node_id} at {gen_path}")
            continue
        if gen_path is None:
            node_matches = False
            diffs.append(f"missing node {node_id}")
            continue
        ref_sig = _node_signature(ref_path)
        gen_sig = _node_signature(gen_path)
        if ref_sig != gen_sig:
            node_matches = False
            diffs.append(f"node metadata differs for {node_id}")
            if compare_body and ref_path.read_text(encoding="utf-8") != gen_path.read_text(encoding="utf-8"):
                diffs.append(f"node text differs for {node_id}")

    return KnowledgeVerificationResult(
        reference_root=reference_root,
        generated_root=generated_root,
        config_matches=config_matches,
        topic_catalog_matches=topic_catalog_matches,
        node_matches=node_matches,
        diffs=tuple(diffs),
    )


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Verify a generated docs/knowledge tree")
    parser.add_argument("reference_root", type=Path)
    parser.add_argument("generated_root", type=Path)
    parser.add_argument("--compare-body", action="store_true")
    args = parser.parse_args()

    result = verify_knowledge_tree(
        args.reference_root,
        args.generated_root,
        compare_body=args.compare_body,
    )
    print("clean" if result.clean else "dirty")
    for diff in result.diffs:
        print(diff)


if __name__ == "__main__":
    main()
