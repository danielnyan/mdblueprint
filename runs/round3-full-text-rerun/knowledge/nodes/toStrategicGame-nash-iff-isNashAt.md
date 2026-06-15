---
id: toStrategicGame-nash-iff-isNashAt
title: toStrategicGame_nash_iff_isNashAt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeStrategicForm
  declarations:
    - toStrategicGame_nash_iff_isNashAt
uses:
  - toStrategicGame
  - Profile
  - IsNashEquilibrium
  - IsNashAt
  - profileStrategy
  - PlayerStrategy
  - IsWeaklyDominant.isBestResponse
  - IsBestResponse
  - profileStrategy_deviate_eq_of_variant
  - profileStrategy_deviate_variant
---

# toStrategicGame_nash_iff_isNashAt

## Lean type

```lean
theorem toStrategicGame_nash_iff_isNashAt (g : GameTree N U) (σ : (toStrategicGame g).Profile) : _root_.IsNashEquilibrium (toStrategicGame g) σ ↔ IsNashAt (profileStrategy σ) g
```

## Dependencies

- toStrategicGame
- Profile
- IsNashEquilibrium
- IsNashAt
- profileStrategy
- PlayerStrategy
- IsWeaklyDominant.isBestResponse
- IsBestResponse
- profileStrategy_deviate_eq_of_variant
- profileStrategy_deviate_variant
