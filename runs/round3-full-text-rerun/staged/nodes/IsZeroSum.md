---
id: IsZeroSum
title: IsZeroSum
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsZeroSum
uses:
  - Profile
---

# IsZeroSum

## Lean type

```lean
def IsZeroSum [Add U] [Zero U] (G : StrategicGame (Fin 2) U) : Prop
```

## Dependencies

- Profile
