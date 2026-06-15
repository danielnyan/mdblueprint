---
id: mu-aux-lt-iff-lt
title: mu.aux_lt_iff_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - mu.aux_lt_iff_lt
uses:
---

# mu.aux_lt_iff_lt

## Lean type

```lean
theorem mu.aux_lt_iff_lt (A : I → J → ℝ) (c : ℝ) (y : stdSimplex ℝ J) : mu.aux A y < c ↔ ∀ i, wsum y (fun j => A i j) < c
```

## Dependencies

- none
