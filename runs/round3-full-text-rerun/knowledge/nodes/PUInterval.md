---
id: PUInterval
title: PUInterval
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.ZeroSumGameTreeWithChance
  declarations:
    - PUInterval
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
---

# PUInterval

## Lean type

```lean
def PUInterval (a : ℚ) : Set.Icc (0 : ℚ) 1
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
