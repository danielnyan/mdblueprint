#!/usr/bin/env python3
"""Generate Lean-derived draft node files for a bounded sample.

This script is intentionally narrow: it emits a small set of representative
draft nodes that were selected in the study notes and are useful for testing
how much node metadata Lean can recover on its own.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mdblueprint.knowledge_uses import inferred_uses
from tools.knowledge.lean_index import LeanDeclaration, index_lean_project
from tools.knowledge.parser import parse_file


@dataclass(frozen=True)
class SampleCase:
    node_id: str
    declarations: tuple[str, ...]


SAMPLE_CASES: tuple[SampleCase, ...] = (
    SampleCase(
        "social_choice.fair_division.divisible.proportional_exists",
        ("SocialChoice.FairDivision.Divisible.proportional_exists",),
    ),
    SampleCase(
        "social_choice.fair_division.indivisible.round_robin_alloc",
        (
            "SocialChoice.FairDivision.Indivisible.roundRobinAux",
            "SocialChoice.FairDivision.Indivisible.roundRobinAllocation",
            "SocialChoice.FairDivision.Indivisible.roundRobinRule",
        ),
    ),
    SampleCase(
        "game_theory.strategic_game.equilibrium.nash_existence_finite_games",
        ("StrategicGame.exists_mixed_nash_equilibrium_finite",),
    ),
    SampleCase(
        "social_choice.fair_division.indivisible.maximin_share",
        ("SocialChoice.FairDivision.Indivisible.IsMaxminShare",),
    ),
    SampleCase(
        "math.minimax.common_guarantee_value",
        ("MatrixGame.common_guarantee_eq_value",),
    ),
    SampleCase(
        "foundation.cost.examples.reverse_space",
        ("ReverseSpace.naiveReverse", "ReverseSpace.naiveReverse_cost_le"),
    ),
)


def _title_from_decl(decls: list[LeanDeclaration], node_id: str) -> str:
    for decl in decls:
        if decl.docstring:
            first = decl.docstring.splitlines()[0].strip()
            if first:
                return first
    leaf = node_id.rsplit(".", 1)[-1]
    return re.sub(r"[_-]+", " ", leaf).title()


def _topic_chain(node_id: str) -> list[str]:
    parts = node_id.split(".")
    if not parts:
        return [node_id]
    out = [parts[0]]
    if len(parts) >= 2:
        out.append(".".join(parts[:2]))
    if len(parts) >= 3 and parts[0] == "game_theory":
        out.append(".".join(parts[:3]))
    return list(dict.fromkeys(out))


def _kind_from_decls(decls: list[LeanDeclaration]) -> str:
    return "theorem" if any(d.kind in {"theorem", "lemma"} for d in decls) else "definition"


def _status_from_decls(decls: list[LeanDeclaration]) -> str:
    return "staged" if any(d.has_sorry for d in decls) else ("proved" if any(d.kind in {"theorem", "lemma"} for d in decls) else "formalized")


def _modules_from_decls(decls: list[LeanDeclaration]) -> list[str]:
    modules: list[str] = []
    for decl in decls:
        if decl.module and decl.module not in modules:
            modules.append(decl.module)
    return modules


def _render(node_id: str, decls: list[LeanDeclaration], uses: list[str]) -> str:
    payload = {
        "id": node_id,
        "title": _title_from_decl(decls, node_id),
        "kind": _kind_from_decls(decls),
        "status": _status_from_decls(decls),
        "uses": uses,
        "primary_topic": node_id.split(".", 1)[0],
        "topics": _topic_chain(node_id),
        "lean": {
            "modules": _modules_from_decls(decls),
            "declarations": [d.qualified_name for d in decls],
        },
    }
    body = ["Generated from Lean source only.", "", "## Lean Evidence"]
    for decl in decls:
        body.append(f"- `{decl.qualified_name}` in `{decl.module or decl.file.name}` ({decl.kind})")
        if decl.docstring:
            body.append(f"  - {decl.docstring}")
    return "---\n" + yaml.safe_dump(payload, sort_keys=False, allow_unicode=True).rstrip() + "\n---\n\n" + "\n".join(body).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate representative Lean-derived node drafts")
    parser.add_argument("--lean-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--knowledge-root", type=Path, help="Existing docs/knowledge tree used only as a node/declaration index for uses inference")
    args = parser.parse_args()

    idx = index_lean_project(args.lean_root)
    reference_nodes = []
    if args.knowledge_root is not None:
        for base in (args.knowledge_root / "nodes", args.knowledge_root / "staged"):
            if base.is_dir():
                reference_nodes.extend(parse_file(path) for path in sorted(base.rglob("*.md")) if path.name != "topics.md")

    if args.output.exists():
        shutil.rmtree(args.output)
    args.output.mkdir(parents=True, exist_ok=True)

    for case in SAMPLE_CASES:
        decls = []
        for decl_name in case.declarations:
            decl = idx.declarations.get(decl_name)
            if decl is not None:
                decls.append(decl)
        if not decls:
            continue
        uses: list[str] = []
        if reference_nodes:
            source = next((node for node in reference_nodes if node.id == case.node_id), None)
            if source is not None:
                uses = inferred_uses(source, reference_nodes, idx)
        path = args.output / f"{case.node_id.replace('.', '_')}.md"
        path.write_text(_render(case.node_id, decls, uses), encoding="utf-8")
        print(path)


if __name__ == "__main__":
    main()
