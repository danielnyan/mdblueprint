---
id: IsStrictlyDominant
title: IsStrictlyDominant
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Dominance
  declarations:
    - IsStrictlyDominant
uses:
  - Strategy
  - StrictlyDominates
---

# IsStrictlyDominant

## Lean type

```lean
def IsStrictlyDominant (G : StrategicGame N U) (i : N) (s : G.strategy i) : Prop
```

## Dependencies

- Strategy
- StrictlyDominates
