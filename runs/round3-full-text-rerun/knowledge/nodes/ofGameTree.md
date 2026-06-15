---
id: ofGameTree
title: ofGameTree
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.StochasticGameTree
  declarations:
    - ofGameTree
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
---

# ofGameTree

## Lean type

```lean
def ofGameTree : GameTree N ℚ → StochasticGameTree N | GameTree.Leaf p => StochasticGameTree.Leaf p | GameTree.Node m h t => StochasticGameTree.Player m (ofGameTree h) (t.map ofGameTree) /-- Local probability mass check at a chance node. -/
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
