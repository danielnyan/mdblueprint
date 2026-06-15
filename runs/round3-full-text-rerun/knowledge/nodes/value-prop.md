---
id: value-prop
title: value_prop
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.ZeroSumGameTreeWithChance
  declarations:
    - value_prop
uses:
  - Strategy
  - DStrategy
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# value_prop

## Lean type

```lean
theorem value_prop (SB : Strategy) {t : GameTree} : t.value ≤ t.outcome DStrategy SB
```

## Dependencies

- Strategy
- DStrategy
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
