---
id: candidateChoiceGame
title: candidateChoiceGame
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CandidateChoice
  declarations:
    - candidateChoiceGame
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - larryChoice
  - majorityOutcome
  - majorityOutcome_pairwise_distinct
  - sergeyChoice
  - IsZeroSum.tail_mem
  - Subtree.tail_mem
---

# candidateChoiceGame

## Lean type

```lean
def candidateChoiceGame : GameTree Player ℚ
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- larryChoice
- majorityOutcome
- majorityOutcome_pairwise_distinct
- sergeyChoice
- IsZeroSum.tail_mem
- Subtree.tail_mem
