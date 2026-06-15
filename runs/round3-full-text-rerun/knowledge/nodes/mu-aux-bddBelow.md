---
id: mu-aux-bddBelow
title: mu.aux.bddBelow
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - mu.aux.bddBelow
uses:
  - wsum_const
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - wsum_le_wsum
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# mu.aux.bddBelow

## Lean type

```lean
theorem mu.aux.bddBelow (A : I → J → ℝ) : ∃ C, ∀ y, C ≤ mu.aux A y
```

## Dependencies

- wsum_const
- IsPositiveAffineOf.symm
- Indifferent.symm
- wsum_le_wsum
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
