---
id: sample-optStrategy-spe-on
title: sample_optStrategy_spe_on
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - sample_optStrategy_spe_on
uses:
  - IsSubgamePerfectOn
  - Strategy
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - IsSubgamePerfect.toSubgamePerfectOn
  - optStrategy_isSubgamePerfect
---

# sample_optStrategy_spe_on

## Lean type

```lean
theorem sample_optStrategy_spe_on : IsSubgamePerfectOn (optStrategy : Strategy Player ℚ) sample
```

## Dependencies

- IsSubgamePerfectOn
- Strategy
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- IsSubgamePerfect.toSubgamePerfectOn
- optStrategy_isSubgamePerfect
