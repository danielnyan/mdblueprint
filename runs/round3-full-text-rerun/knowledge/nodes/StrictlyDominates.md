---
id: StrictlyDominates
title: StrictlyDominates
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Dominance
  declarations:
    - StrictlyDominates
uses:
  - Strategy
  - Profile
---

# StrictlyDominates

## Lean type

```lean
def StrictlyDominates (G : StrategicGame N U) (i : N) (s s' : G.strategy i) : Prop
```

## Dependencies

- Strategy
- Profile
