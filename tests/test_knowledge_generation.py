from __future__ import annotations

import textwrap
from pathlib import Path

from mdblueprint.knowledge_generation import generate_knowledge_tree
from mdblueprint.knowledge_verification import verify_knowledge_tree


def _write_minimal_reference(reference_root: Path) -> None:
    (reference_root / "nodes" / "analysis").mkdir(parents=True)
    (reference_root / "mdblueprint.yml").write_text(
        textwrap.dedent(
            """
            site:
              title: Example Blueprint
            topics:
              - id: analysis
                title: Analysis
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )
    (reference_root / "nodes" / "analysis" / "limit.md").write_text(
        textwrap.dedent(
            """
            ---
            id: analysis.limit_unique
            title: Limit Is Unique
            kind: theorem
            status: admitted
            uses: []
            primary_topic: analysis
            topics:
              - analysis
            lean:
              modules:
                - Analysis.Limit
              declarations:
                - Analysis.limit_unique
            ---

            # Limit Is Unique

            A deterministic theorem.
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )
    (reference_root / "Analysis").mkdir(parents=True)
    (reference_root / "Analysis" / "Limit.lean").write_text(
        textwrap.dedent(
            """
            namespace Analysis

            theorem limit_unique : True := by
              trivial

            end Analysis
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )


def test_refresh_round_trip_preserves_metadata(tmp_path):
    reference_root = tmp_path / "reference"
    output_root = tmp_path / "output"
    _write_minimal_reference(reference_root)

    result = generate_knowledge_tree(
        lean_root=reference_root,
        output_root=output_root,
        reference_root=reference_root,
    )

    assert result.refreshed_from_reference is True
    assert (output_root / "mdblueprint.yml").exists()
    verification = verify_knowledge_tree(reference_root, output_root)
    assert verification.clean, verification.diffs
