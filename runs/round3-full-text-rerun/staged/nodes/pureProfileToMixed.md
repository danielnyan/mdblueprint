---
id: pureProfileToMixed
title: pureProfileToMixed
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - pureProfileToMixed
uses:
  - Strategy
  - Profile
  - MixedProfile
  - pureToMixed
---

# pureProfileToMixed

## Lean type

```lean
def pureProfileToMixed {G : StrategicGame N U} [∀ i, Fintype (G.strategy i)] [∀ i, DecidableEq (G.strategy i)] (σ : G.Profile) : MixedProfile G
```

## Dependencies

- Strategy
- Profile
- MixedProfile
- pureToMixed
