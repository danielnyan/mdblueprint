---
id: IsDegenerateCorrelatedEq
title: IsDegenerateCorrelatedEq
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.CorrelatedEq
  declarations:
    - IsDegenerateCorrelatedEq
uses:
  - Profile
  - IsNashEquilibrium
---

# IsDegenerateCorrelatedEq

## Lean type

```lean
def IsDegenerateCorrelatedEq (G : StrategicGame N U) (σ : G.Profile) : Prop
```

## Dependencies

- Profile
- IsNashEquilibrium
