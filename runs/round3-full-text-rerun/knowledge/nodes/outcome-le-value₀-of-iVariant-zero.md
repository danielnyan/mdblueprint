---
id: outcome-le-value₀-of-iVariant-zero
title: outcome_le_value₀_of_iVariant_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - outcome_le_value₀_of_iVariant_zero
uses:
  - Strategy
  - IVariant
  - optStrategy_isSubgamePerfect
  - outcome_optStrategy_eq_value
---

# outcome_le_value₀_of_iVariant_zero

## Lean type

```lean
theorem outcome_le_value₀_of_iVariant_zero (g : GameTree (Fin 2) ℚ) {σ' : Strategy (Fin 2) ℚ} (hiv : IVariant (0 : Fin 2) optStrategy σ') : outcome σ' g 0 ≤ value₀ g
```

## Dependencies

- Strategy
- IVariant
- optStrategy_isSubgamePerfect
- outcome_optStrategy_eq_value
