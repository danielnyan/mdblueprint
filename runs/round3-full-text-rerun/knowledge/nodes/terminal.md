---
id: terminal
title: terminal
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - terminal
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
---

# terminal

## Lean type

```lean
def terminal (o : Outcome) : GameTree Player ℚ
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
