---
id: sample
title: sample
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - sample
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - zeroSumLeaf
---

# sample

## Lean type

```lean
def sample : GameTree Player ℚ
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- zeroSumLeaf
