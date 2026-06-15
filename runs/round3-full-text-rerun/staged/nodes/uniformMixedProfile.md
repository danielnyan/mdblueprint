---
id: uniformMixedProfile
title: uniformMixedProfile
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - uniformMixedProfile
uses:
  - Strategy
  - MixedProfile
  - uniformMixed
---

# uniformMixedProfile

## Lean type

```lean
def uniformMixedProfile (G : StrategicGame N ℚ) [∀ i, Fintype (G.strategy i)] [∀ i, Nonempty (G.strategy i)] : MixedProfile G
```

## Dependencies

- Strategy
- MixedProfile
- uniformMixed
