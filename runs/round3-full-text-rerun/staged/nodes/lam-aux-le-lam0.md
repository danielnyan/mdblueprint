---
id: lam-aux-le-lam0
title: lam.aux.le_lam0
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - lam.aux.le_lam0
uses:
  - lamB.aux.bddAbove
  - lam.aux.bddAbove
---

# lam.aux.le_lam0

## Lean type

```lean
theorem lam.aux.le_lam0 (A : I → J → ℝ) (x : stdSimplex ℝ I) : lam.aux A x ≤ lam0 A
```

## Dependencies

- lamB.aux.bddAbove
- lam.aux.bddAbove
