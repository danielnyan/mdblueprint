---
id: profileStrategy-deviate-variant
title: profileStrategy_deviate_variant
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeStrategicForm
  declarations:
    - profileStrategy_deviate_variant
uses:
  - PlayerStrategy
  - IVariant
  - profileStrategy
---

# profileStrategy_deviate_variant

## Lean type

```lean
theorem profileStrategy_deviate_variant (σ : N → PlayerStrategy N U) (i : N) (s' : PlayerStrategy N U) : IVariant i (profileStrategy σ) (profileStrategy (Function.update σ i s'))
```

## Dependencies

- PlayerStrategy
- IVariant
- profileStrategy
