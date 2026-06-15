---
id: utility
title: utility
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - utility
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
---

# utility

## Lean type

```lean
def utility : Player → Outcome → ℚ | Eric, Accepted Lee => 3 | Eric, Accepted Rebecca => 2 | Eric, Accepted John => 1 | Eric, Rejected => 0 | Larry, Accepted Rebecca => 3 | Larry, Accepted John => 2 | Larry, Accepted Lee => 1 | Larry, Rejected => 0 | Sergey, Accepted John => 3 | Sergey, Accepted Lee => 2 | Sergey, Accepted Rebecca => 1 | Sergey, Rejected => 0 /-- Convert an outcome into the payoff vector required by `GameTree`. -/
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
