"""Extension point for semantic theorem renaming.

The current Lean-backed dependency inference uses exact Lean declaration names
and conservative aliases. Future work can plug in a theorem renamer here to
add semantic aliases when declaration names are uninformative or unstable.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from tools.knowledge.lean_index import LeanDeclaration


@dataclass(frozen=True)
class TheoremNameCandidate:
    """One proposed semantic name or alias for a Lean declaration."""

    name: str
    confidence: float = 1.0
    reason: str = "unspecified"


@dataclass(frozen=True)
class TheoremRenamingResult:
    """Renamer output for one declaration."""

    canonical_name: str | None = None
    aliases: tuple[TheoremNameCandidate, ...] = ()


class TheoremRenamer(Protocol):
    """Protocol implemented by future theorem-renaming providers."""

    def rename(self, declaration: LeanDeclaration) -> TheoremRenamingResult:
        """Return semantic aliases for ``declaration``."""


class IdentityTheoremRenamer:
    """Default renamer that preserves current behavior."""

    def rename(self, declaration: LeanDeclaration) -> TheoremRenamingResult:
        return TheoremRenamingResult(canonical_name=declaration.qualified_name)


def renaming_aliases_for_declaration(
    declaration: LeanDeclaration,
    renamer: TheoremRenamer,
    *,
    min_confidence: float = 0.75,
) -> tuple[str, ...]:
    """Return safe aliases emitted by ``renamer`` for dependency matching."""
    result = renamer.rename(declaration)
    aliases: list[str] = []
    if result.canonical_name and result.canonical_name != declaration.qualified_name:
        aliases.append(result.canonical_name)
    for candidate in result.aliases:
        if candidate.confidence >= min_confidence and candidate.name:
            aliases.append(candidate.name)
    return tuple(dict.fromkeys(aliases))
