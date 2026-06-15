---
id: IsCompletelyMixedProfile-player
title: IsCompletelyMixedProfile.player
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.MixedStrategy
  declarations:
    - IsCompletelyMixedProfile.player
uses:
  - Strategy
  - MixedProfile
  - IsCompletelyMixedProfile
  - IsCompletelyMixed
---

# IsCompletelyMixedProfile.player

## Lean type

```lean
theorem IsCompletelyMixedProfile.player {G : StrategicGame N ℚ} [∀ i, Fintype (G.strategy i)] {p : MixedProfile G} (hp : IsCompletelyMixedProfile G p) (i : N) : IsCompletelyMixed G (p i)
```

## Dependencies

- Strategy
- MixedProfile
- IsCompletelyMixedProfile
- IsCompletelyMixed
