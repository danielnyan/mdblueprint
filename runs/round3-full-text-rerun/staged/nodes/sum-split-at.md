---
id: sum-split-at
title: sum_split_at
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - sum_split_at
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# sum_split_at

## Lean type

```lean
theorem sum_split_at [DecidableEq J] (j₀ : J) (f : J → ℝ) : ∑ j : J, f j = f j₀ + ∑ j' : {j : J // j ≠ j₀}, f j'.val
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
