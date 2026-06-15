---
id: larryChoice
title: larryChoice
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - larryChoice
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - sergeyChoice
---

# larryChoice

## Lean type

```lean
def larryChoice (ericVote : Candidate) : GameTree Player ℚ
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- sergeyChoice
