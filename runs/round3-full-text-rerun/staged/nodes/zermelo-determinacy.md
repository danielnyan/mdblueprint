---
id: zermelo-determinacy
title: zermelo_determinacy
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - zermelo_determinacy
uses:
  - IsZeroSum
  - Strategy
  - IVariant
  - value₀_le_outcome_of_iVariant_one
  - outcome_le_value₀_of_iVariant_zero
---

# zermelo_determinacy

## Lean type

```lean
theorem zermelo_determinacy (g : GameTree (Fin 2) ℚ) (hzs : IsZeroSum g) : (∀ σ' : Strategy (Fin 2) ℚ, IVariant (1 : Fin 2) optStrategy σ' → value₀ g ≤ outcome σ' g 0) ∧ (∀ σ' : Strategy (Fin 2) ℚ, IVariant (0 : Fin 2) optStrategy σ' → outcome σ' g 0 ≤ value₀ g)
```

## Dependencies

- IsZeroSum
- Strategy
- IVariant
- value₀_le_outcome_of_iVariant_one
- outcome_le_value₀_of_iVariant_zero
