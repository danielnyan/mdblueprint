---
id: IsExactPotential
title: IsExactPotential
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.PotentialGame
  declarations:
    - IsExactPotential
uses:
  - Profile
  - Strategy
---

# IsExactPotential

## Lean type

```lean
def IsExactPotential (G : StrategicGame N U) (Φ : G.Profile → U) : Prop
```

## Dependencies

- Profile
- Strategy
