---
id: outcome-optStrategy-zero-sum
title: outcome_optStrategy_zero_sum
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - outcome_optStrategy_zero_sum
uses:
  - IsZeroSum
  - Strategy
  - outcome_zero_sum
---

# outcome_optStrategy_zero_sum

## Lean type

```lean
theorem outcome_optStrategy_zero_sum (g : GameTree (Fin 2) ℚ) (hzs : IsZeroSum g) : outcome (optStrategy : Strategy (Fin 2) ℚ) g 0 + outcome (optStrategy : Strategy (Fin 2) ℚ) g 1 = 0
```

## Dependencies

- IsZeroSum
- Strategy
- outcome_zero_sum
