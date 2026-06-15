---
id: optimalColumnSet-nonempty
title: optimalColumnSet_nonempty
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.OptimalStrategySetPolytope
  declarations:
    - optimalColumnSet_nonempty
uses:
  - minimax_optimal_strategies
  - lamB.aux.bddAbove
  - lam.aux.bddAbove
  - muB.aux.bddBelow
  - mu.aux.bddBelow
  - maximin_le_minimax
  - value_eq_maximin
---

# optimalColumnSet_nonempty

## Lean type

```lean
theorem optimalColumnSet_nonempty : A.optimalColumnSet.Nonempty
```

## Dependencies

- minimax_optimal_strategies
- lamB.aux.bddAbove
- lam.aux.bddAbove
- muB.aux.bddBelow
- mu.aux.bddBelow
- maximin_le_minimax
- value_eq_maximin
