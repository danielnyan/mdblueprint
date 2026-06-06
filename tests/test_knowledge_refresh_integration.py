from __future__ import annotations

from pathlib import Path

import pytest

from mdblueprint.knowledge_generation import generate_knowledge_tree
from mdblueprint.knowledge_verification import verify_knowledge_tree


@pytest.mark.integration
def test_econcslib_can_be_refreshed_and_verified(econcslib_checkout, tmp_path):
    repo = Path(econcslib_checkout)
    reference_root = repo / "docs" / "knowledge"
    lean_root = repo / "EconCSLib"
    output_root = tmp_path / "refreshed"

    result = generate_knowledge_tree(
        lean_root=lean_root,
        output_root=output_root,
        reference_root=reference_root,
    )

    assert result.refreshed_from_reference is True
    verification = verify_knowledge_tree(reference_root, output_root)
    assert verification.clean, verification.diffs
