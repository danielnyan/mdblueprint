---
id: total-mass-preserved
title: total_mass_preserved
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.StochasticMatrix
  declarations:
    - total_mass_preserved
uses:
  - value_eq_minimax
  - muB.aux.bddBelow
  - mu.aux.bddBelow
---

# total_mass_preserved

## Lean type

```lean
theorem total_mass_preserved (hA : IsStochasticMatrix A) (x : I → ℝ) : ∑ j, ∑ i, x i * A i j = ∑ i, x i
```

## Dependencies

- value_eq_minimax
- muB.aux.bddBelow
- mu.aux.bddBelow
