---
id: MixedProfile
title: MixedProfile
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - MixedProfile
uses:
  - Strategy
  - MixedStrategy
---

# MixedProfile

## Lean type

```lean
def MixedProfile (G : StrategicGame N U) [∀ i, Fintype (G.strategy i)]
```

## Dependencies

- Strategy
- MixedStrategy
