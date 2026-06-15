---
id: IsBestResponse
title: IsBestResponse
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.BestResponse
  declarations:
    - IsBestResponse
uses:
  - Profile
  - Strategy
---

# IsBestResponse

## Lean type

```lean
def IsBestResponse (G : StrategicGame N U) (σ : G.Profile) (i : N) : Prop
```

## Dependencies

- Profile
- Strategy
