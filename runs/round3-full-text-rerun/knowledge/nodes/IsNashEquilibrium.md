---
id: IsNashEquilibrium
title: IsNashEquilibrium
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.NashEquilibrium
  declarations:
    - IsNashEquilibrium
uses:
  - Strategy
  - IVariant
  - Profile
  - IsWeaklyDominant.isBestResponse
  - IsBestResponse
---

# IsNashEquilibrium

## Lean type

```lean
def IsNashEquilibrium (G : StrategicGame N U) (σ : G.Profile) : Prop
```

## Dependencies

- Strategy
- IVariant
- Profile
- IsWeaklyDominant.isBestResponse
- IsBestResponse
