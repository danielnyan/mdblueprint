---
id: value₀-le-outcome-of-iVariant-one
title: value₀_le_outcome_of_iVariant_one
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value₀_le_outcome_of_iVariant_one
uses:
  - IsZeroSum
  - Strategy
  - IVariant
  - optStrategy_isSubgamePerfect
  - outcome_optStrategy_eq_value
  - value_one_eq_neg_value₀
  - outcome_zero_sum
---

# value₀_le_outcome_of_iVariant_one

## Lean type

```lean
theorem value₀_le_outcome_of_iVariant_one (g : GameTree (Fin 2) ℚ) (hzs : IsZeroSum g) {σ' : Strategy (Fin 2) ℚ} (hiv : IVariant (1 : Fin 2) optStrategy σ') : value₀ g ≤ outcome σ' g 0
```

## Dependencies

- IsZeroSum
- Strategy
- IVariant
- optStrategy_isSubgamePerfect
- outcome_optStrategy_eq_value
- value_one_eq_neg_value₀
- outcome_zero_sum
