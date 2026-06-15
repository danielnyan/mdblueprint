---
id: tiny
title: tiny
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.ImperfectInformation
  declarations:
    - tiny
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - IsReachable.next
  - ReachedSubgamePayoffTransfer.init
---

# tiny

## Lean type

```lean
def tiny : FiniteImperfectGame Player ℤ
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- IsReachable.next
- ReachedSubgamePayoffTransfer.init
