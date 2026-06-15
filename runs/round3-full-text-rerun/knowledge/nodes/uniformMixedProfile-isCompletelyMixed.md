---
id: uniformMixedProfile-isCompletelyMixed
title: uniformMixedProfile_isCompletelyMixed
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - uniformMixedProfile_isCompletelyMixed
uses:
  - Strategy
  - IsCompletelyMixedProfile
  - uniformMixedProfile
  - uniformMixed_isCompletelyMixed
---

# uniformMixedProfile_isCompletelyMixed

## Lean type

```lean
theorem uniformMixedProfile_isCompletelyMixed (G : StrategicGame N ℚ) [∀ i, Fintype (G.strategy i)] [∀ i, Nonempty (G.strategy i)] : IsCompletelyMixedProfile G (uniformMixedProfile G)
```

## Dependencies

- Strategy
- IsCompletelyMixedProfile
- uniformMixedProfile
- uniformMixed_isCompletelyMixed
