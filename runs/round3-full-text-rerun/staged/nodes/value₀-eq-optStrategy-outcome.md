---
id: value₀-eq-optStrategy-outcome
title: value₀_eq_optStrategy_outcome
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value₀_eq_optStrategy_outcome
uses:
  - Strategy
  - outcome_optStrategy_eq_value
---

# value₀_eq_optStrategy_outcome

## Lean type

```lean
theorem value₀_eq_optStrategy_outcome (g : GameTree (Fin 2) ℚ) : value₀ g = outcome (optStrategy : Strategy (Fin 2) ℚ) g 0
```

## Dependencies

- Strategy
- outcome_optStrategy_eq_value
