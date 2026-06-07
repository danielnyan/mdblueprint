from __future__ import annotations

from pathlib import Path

from mdblueprint.knowledge_uses import build_uses_inference_context
from mdblueprint.theorem_renaming import TheoremNameCandidate, TheoremRenamingResult
from tools.knowledge.lean_index import LeanDeclaration, LeanIndex


class FakeRenamer:
    def rename(self, declaration: LeanDeclaration) -> TheoremRenamingResult:
        return TheoremRenamingResult(
            canonical_name="semantic.optimizer_existence",
            aliases=(
                TheoremNameCandidate(
                    "optimizer existence theorem",
                    confidence=0.92,
                    reason="test alias",
                ),
                TheoremNameCandidate(
                    "low confidence noise",
                    confidence=0.2,
                    reason="test rejection",
                ),
            ),
        )


def test_theorem_renamer_aliases_are_added_to_reference_index():
    declaration = LeanDeclaration(
        name="opaque_name",
        qualified_name="Library.Section.opaque_name",
        kind="theorem",
        file=Path("Library/Section.lean"),
        line=1,
    )
    idx = LeanIndex(declarations={declaration.qualified_name: declaration})

    context = build_uses_inference_context([], idx, theorem_renamer=FakeRenamer())

    assert context.reference_index["Library.Section.opaque_name"] == [
        "Library.Section.opaque_name"
    ]
    assert context.reference_index["semantic.optimizer_existence"] == [
        "Library.Section.opaque_name"
    ]
    assert context.reference_index["optimizer existence theorem"] == [
        "Library.Section.opaque_name"
    ]
    assert "low confidence noise" not in context.reference_index
