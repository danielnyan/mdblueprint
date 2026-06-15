---
id: wsum-extendDropColumn
title: wsum_extendDropColumn
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - wsum_extendDropColumn
uses:
  - sum_split_at
---

# wsum_extendDropColumn

## Lean type

```lean
theorem wsum_extendDropColumn [DecidableEq J] (j₀ : J) (y' : stdSimplex ℝ {j : J // j ≠ j₀}) (f : J → ℝ) : wsum (extendDropColumn j₀ y') f = ∑ j' : {j : J // j ≠ j₀}, y'.val j' * f j'.val
```

## Dependencies

- sum_split_at
