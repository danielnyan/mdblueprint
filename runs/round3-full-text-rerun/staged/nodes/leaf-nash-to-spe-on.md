---
id: leaf-nash-to-spe-on
title: leaf_nash_to_spe_on
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.SimpleGameTree
  declarations:
    - leaf_nash_to_spe_on
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - Strategy
  - IsNashAt
  - IsSubgamePerfectOn
  - IsNashAt.toSubgamePerfectOn_of_hasOnlyRootSubgames
  - leaf_hasOnlyRootSubgames
---

# leaf_nash_to_spe_on

## Lean type

```lean
theorem leaf_nash_to_spe_on (p : Player → ℚ) {σ : Strategy Player ℚ} (hnash : GameTree.IsNashAt σ (Leaf p)) : IsSubgamePerfectOn σ (Leaf p)
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- Strategy
- IsNashAt
- IsSubgamePerfectOn
- IsNashAt.toSubgamePerfectOn_of_hasOnlyRootSubgames
- leaf_hasOnlyRootSubgames
