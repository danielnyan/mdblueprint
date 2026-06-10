from __future__ import annotations

import textwrap
from pathlib import Path

from mdblueprint.knowledge_uses import InferredUse, inferred_uses, infer_uses_for_node, infer_and_review_uses_for_nodes
from tools.knowledge.lean_index import index_lean_project
from tools.knowledge.models import LeanRef, Node


def _write_lean(root: Path) -> None:
    (root / "Logic").mkdir(parents=True)
    (root / "Logic" / "Main.lean").write_text(
        textwrap.dedent(
            """
            namespace Logic

            theorem base : True := by
              trivial

            private theorem helper : True := by
              exact base

            theorem result : True := by
              exact helper

            theorem body_ref_result : True := by
              trivial

            end Logic
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )


def _node(node_id: str, declarations: list[str], *, body: str = "") -> Node:
    return Node(
        id=node_id,
        title=node_id,
        kind="theorem",
        status="proved",
        uses=[],
        lean=LeanRef(modules=["Logic.Main"], declarations=declarations),
        body=body,
    )


def test_infers_transitive_lean_decl_dependency(tmp_path):
    _write_lean(tmp_path)
    idx = index_lean_project(tmp_path)
    base = _node("logic.base", ["Logic.base"])
    result = _node("logic.result", ["Logic.result"])

    assert inferred_uses(result, [base, result], idx) == ["logic.base"]
    evidence = infer_uses_for_node(result, [base, result], idx)[0]
    assert evidence.evidence == "lean_transitive_decl"
    assert evidence.via == ("Logic.result", "Logic.helper", "Logic.base")


def test_review_flags_body_node_refs_without_removing_them(tmp_path):
    _write_lean(tmp_path)
    idx = index_lean_project(tmp_path)
    base = _node("logic.base", ["Logic.base"])
    result = _node(
        "logic.body_ref_result",
        ["Logic.body_ref_result"],
        body="Proof. By [[node:logic.base]].",
    )

    review = infer_and_review_uses_for_nodes([base, result], idx)
    assert [item.target_node_id for item in review.retained_by_node["logic.body_ref_result"]] == ["logic.base"]
    assert [item.evidence for item in review.problematic_by_node["logic.body_ref_result"]] == ["body_node_ref"]


def test_review_flags_cycles_without_pruning_edges():
    uses_by_node = {
        "a": [InferredUse("a", "b", "lean_direct_decl", ("A.a", "A.b"))],
        "b": [InferredUse("b", "c", "lean_direct_decl", ("B.b", "B.c"))],
        "c": [InferredUse("c", "a", "lean_transitive_decl", ("C.c", "C.helper", "A.a"))],
    }

    from mdblueprint.knowledge_uses import review_redundant_inferred_uses

    review = review_redundant_inferred_uses(uses_by_node)
    assert [item.target_node_id for item in review.retained_by_node["c"]] == ["a"]
    assert [item.evidence for item in review.problematic_by_node["c"]] == ["lean_transitive_decl"]
