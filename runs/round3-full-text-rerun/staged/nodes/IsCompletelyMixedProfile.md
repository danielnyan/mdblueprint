---
id: IsCompletelyMixedProfile
title: IsCompletelyMixedProfile
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - IsCompletelyMixedProfile
uses:
  - Strategy
  - MixedProfile
  - IsCompletelyMixed
---

# IsCompletelyMixedProfile

## Lean type

```lean
def IsCompletelyMixedProfile (G : StrategicGame N ℚ) [∀ i, Fintype (G.strategy i)] (p : MixedProfile G) : Prop
```

## Dependencies

- Strategy
- MixedProfile
- IsCompletelyMixed
