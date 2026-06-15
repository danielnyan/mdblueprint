---
id: expectedPayoff
title: expectedPayoff
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - expectedPayoff
uses:
  - Strategy
  - MixedProfile
  - Profile
---

# expectedPayoff

## Lean type

```lean
def expectedPayoff (G : StrategicGame N U) [Fintype N] [DecidableEq N] [∀ i, Fintype (G.strategy i)] (p : MixedProfile G) (who : N) : U
```

## Dependencies

- Strategy
- MixedProfile
- Profile
