---
id: sample-strategic-form-has-nash
title: sample_strategic_form_has_nash
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - sample_strategic_form_has_nash
uses:
  - toStrategicGame
  - Profile
  - IsNashEquilibrium
  - IsNashAt
  - profileStrategy
  - Strategy
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - toStrategicGame_nash_iff_isNashAt
  - optStrategy_isSubgamePerfect
  - IsSubgamePerfect.toNE
---

# sample_strategic_form_has_nash

## Lean type

```lean
theorem sample_strategic_form_has_nash : ∃ σ : (toStrategicGame sample).Profile, IsNashEquilibrium (toStrategicGame sample) σ ∧ IsNashAt (profileStrategy σ) sample
```

## Dependencies

- toStrategicGame
- Profile
- IsNashEquilibrium
- IsNashAt
- profileStrategy
- Strategy
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- toStrategicGame_nash_iff_isNashAt
- optStrategy_isSubgamePerfect
- IsSubgamePerfect.toNE
