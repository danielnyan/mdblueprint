---
id: outcome-optStrategy-one-eq-neg-value₀
title: outcome_optStrategy_one_eq_neg_value₀
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - outcome_optStrategy_one_eq_neg_value₀
uses:
  - IsZeroSum
  - Strategy
  - outcome_optStrategy_eq_value
  - value_one_eq_neg_value₀
---

# outcome_optStrategy_one_eq_neg_value₀

## Lean type

```lean
theorem outcome_optStrategy_one_eq_neg_value₀ (g : GameTree (Fin 2) ℚ) (hzs : IsZeroSum g) : outcome (optStrategy : Strategy (Fin 2) ℚ) g 1 = -value₀ g
```

## Dependencies

- IsZeroSum
- Strategy
- outcome_optStrategy_eq_value
- value_one_eq_neg_value₀
