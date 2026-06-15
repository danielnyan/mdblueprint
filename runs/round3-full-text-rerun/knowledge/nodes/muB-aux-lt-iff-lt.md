---
id: muB-aux-lt-iff-lt
title: muB.aux_lt_iff_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - muB.aux_lt_iff_lt
uses:
---

# muB.aux_lt_iff_lt

## Lean type

```lean
theorem muB.aux_lt_iff_lt (A B : I → J → ℝ) (c : ℝ) (y : stdSimplex ℝ J) : muB.aux A B y < c ↔ ∀ i, rowRatio A B y i < c
```

## Dependencies

- none
