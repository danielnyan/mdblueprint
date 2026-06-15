---
id: sergeyChoice
title: sergeyChoice
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - sergeyChoice
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - majorityOutcome
---

# sergeyChoice

## Lean type

```lean
def sergeyChoice (ericVote larryVote : Candidate) : GameTree Player ℚ
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- majorityOutcome
