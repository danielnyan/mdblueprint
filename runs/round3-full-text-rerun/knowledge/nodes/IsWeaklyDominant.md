---
id: IsWeaklyDominant
title: IsWeaklyDominant
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Dominance
  declarations:
    - IsWeaklyDominant
uses:
  - Strategy
  - WeaklyDominates
---

# IsWeaklyDominant

## Lean type

```lean
def IsWeaklyDominant (G : StrategicGame N U) (i : N) (s : G.strategy i) : Prop
```

## Dependencies

- Strategy
- WeaklyDominates
