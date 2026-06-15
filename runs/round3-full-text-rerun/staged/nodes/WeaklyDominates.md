---
id: WeaklyDominates
title: WeaklyDominates
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Dominance
  declarations:
    - WeaklyDominates
uses:
  - Strategy
  - Profile
---

# WeaklyDominates

## Lean type

```lean
def WeaklyDominates (G : StrategicGame N U) (i : N) (s s' : G.strategy i) : Prop
```

## Dependencies

- Strategy
- Profile
