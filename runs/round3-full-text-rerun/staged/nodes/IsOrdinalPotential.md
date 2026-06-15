---
id: IsOrdinalPotential
title: IsOrdinalPotential
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.PotentialGame
  declarations:
    - IsOrdinalPotential
uses:
  - Profile
  - Strategy
---

# IsOrdinalPotential

## Lean type

```lean
def IsOrdinalPotential (G : StrategicGame N U) (Φ : G.Profile → U) : Prop
```

## Dependencies

- Profile
- Strategy
