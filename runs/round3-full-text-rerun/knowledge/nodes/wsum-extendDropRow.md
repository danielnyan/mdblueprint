---
id: wsum-extendDropRow
title: wsum_extendDropRow
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - wsum_extendDropRow
uses:
  - wsum_extendDropColumn
---

# wsum_extendDropRow

## Lean type

```lean
theorem wsum_extendDropRow [DecidableEq I] (i₀ : I) (x' : stdSimplex ℝ {i : I // i ≠ i₀}) (f : I → ℝ) : wsum (extendDropRow i₀ x') f = ∑ i' : {i : I // i ≠ i₀}, x'.val i' * f i'.val
```

## Dependencies

- wsum_extendDropColumn
