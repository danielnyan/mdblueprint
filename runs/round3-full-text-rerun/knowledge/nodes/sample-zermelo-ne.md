---
id: sample-zermelo-ne
title: sample_zermelo_ne
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - sample_zermelo_ne
uses:
  - Strategy
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - IsNashEquilibrium
  - zermelo_exists_pure_NE
---

# sample_zermelo_ne

## Lean type

```lean
theorem sample_zermelo_ne : ∃ σ : Strategy Player ℚ, GameTree.IsNashEquilibrium σ sample
```

## Dependencies

- Strategy
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- IsNashEquilibrium
- zermelo_exists_pure_NE
