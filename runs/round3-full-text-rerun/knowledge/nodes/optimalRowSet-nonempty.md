---
id: optimalRowSet-nonempty
title: optimalRowSet_nonempty
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.OptimalStrategySetPolytope
  declarations:
    - optimalRowSet_nonempty
uses:
  - minimax_optimal_strategies
  - lamB.aux.bddAbove
  - lam.aux.bddAbove
  - muB.aux.bddBelow
  - mu.aux.bddBelow
  - maximin_le_minimax
  - value_eq_maximin
---

# optimalRowSet_nonempty

## Lean type

```lean
theorem optimalRowSet_nonempty : A.optimalRowSet.Nonempty
```

## Dependencies

- minimax_optimal_strategies
- lamB.aux.bddAbove
- lam.aux.bddAbove
- muB.aux.bddBelow
- mu.aux.bddBelow
- maximin_le_minimax
- value_eq_maximin
