---
id: lam-aux-bddAbove
title: lam.aux.bddAbove
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - lam.aux.bddAbove
uses:
  - wsum_le_wsum
  - wsum_const
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# lam.aux.bddAbove

## Lean type

```lean
theorem lam.aux.bddAbove (A : I → J → ℝ) : ∃ C, ∀ x, lam.aux A x ≤ C
```

## Dependencies

- wsum_le_wsum
- wsum_const
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
