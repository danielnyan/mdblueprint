---
id: sample-zermelo-spe
title: sample_zermelo_spe
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - sample_zermelo_spe
uses:
  - Strategy
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - IsSubgamePerfectOn
  - zermelo_exists_pure_SPE
---

# sample_zermelo_spe

## Lean type

```lean
theorem sample_zermelo_spe : ∃ σ : Strategy Player ℚ, IsSubgamePerfectOn σ sample
```

## Dependencies

- Strategy
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- IsSubgamePerfectOn
- zermelo_exists_pure_SPE
