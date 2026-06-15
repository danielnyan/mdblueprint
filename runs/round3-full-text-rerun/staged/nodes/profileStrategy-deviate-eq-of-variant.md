---
id: profileStrategy-deviate-eq-of-variant
title: profileStrategy_deviate_eq_of_variant
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeStrategicForm
  declarations:
    - profileStrategy_deviate_eq_of_variant
uses:
  - PlayerStrategy
  - Strategy
  - IVariant
  - profileStrategy
---

# profileStrategy_deviate_eq_of_variant

## Lean type

```lean
theorem profileStrategy_deviate_eq_of_variant (σ : N → PlayerStrategy N U) (i : N) (τ : Strategy N U) (hτ : IVariant i (profileStrategy σ) τ) : profileStrategy (Function.update σ i (τ : PlayerStrategy N U)) = τ
```

## Dependencies

- PlayerStrategy
- Strategy
- IVariant
- profileStrategy
