---
id: lamB-aux-le-lamB0
title: lamB.aux.le_lamB0
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - lamB.aux.le_lamB0
uses:
  - IsPositive
  - lamB.aux.bddAbove
  - lam.aux.bddAbove
---

# lamB.aux.le_lamB0

## Lean type

```lean
theorem lamB.aux.le_lamB0 {A B : I → J → ℝ} (hB : IsPositive B) (x : stdSimplex ℝ I) : lamB.aux A B x ≤ lamB0 A B
```

## Dependencies

- IsPositive
- lamB.aux.bddAbove
- lam.aux.bddAbove
