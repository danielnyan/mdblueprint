---
id: leaf-hasOnlyRootSubgames
title: leaf_hasOnlyRootSubgames
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - leaf_hasOnlyRootSubgames
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - HasOnlyRootSubgames
---

# leaf_hasOnlyRootSubgames

## Lean type

```lean
theorem leaf_hasOnlyRootSubgames (p : Player → ℚ) : HasOnlyRootSubgames (Leaf p : GameTree Player ℚ)
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- HasOnlyRootSubgames
