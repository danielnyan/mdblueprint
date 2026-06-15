---
id: IsConstantSum
title: IsConstantSum
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Basic
  declarations:
    - IsConstantSum
uses:
  - Profile
---

# IsConstantSum

## Lean type

```lean
def IsConstantSum [Add U] (G : StrategicGame (Fin 2) U) (c : U) : Prop
```

## Dependencies

- Profile
