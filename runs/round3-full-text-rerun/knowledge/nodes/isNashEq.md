---
id: isNashEq
title: isNashEq
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.Checker
  declarations:
    - isNashEq
uses:
  - Strategy
  - Profile
---

# isNashEq

## Lean type

```lean
def isNashEq [Fintype N] (G : StrategicGame N U) [∀ i, Fintype (G.strategy i)] (σ : G.Profile) : Bool
```

## Dependencies

- Strategy
- Profile
