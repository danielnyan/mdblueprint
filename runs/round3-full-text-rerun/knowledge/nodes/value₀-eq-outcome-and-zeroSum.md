---
id: value₀-eq-outcome-and-zeroSum
title: value₀_eq_outcome_and_zeroSum
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value₀_eq_outcome_and_zeroSum
uses:
  - IsZeroSum
  - Strategy
  - value₀_eq_optStrategy_outcome
  - value_one_eq_neg_value₀
---

# value₀_eq_outcome_and_zeroSum

## Lean type

```lean
theorem value₀_eq_outcome_and_zeroSum (g : GameTree (Fin 2) ℚ) (hzs : IsZeroSum g) : value₀ g = outcome (optStrategy : Strategy (Fin 2) ℚ) g 0 ∧ (value g) 1 = -value₀ g
```

## Dependencies

- IsZeroSum
- Strategy
- value₀_eq_optStrategy_outcome
- value_one_eq_neg_value₀
