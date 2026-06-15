---
id: position-le-card
title: position_le_card
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - position_le_card
uses:
  - rank_lt_card
---

# position_le_card

## Lean type

```lean
theorem position_le_card [Fintype A] (r : LinearOrder A) (a : A) : position r a ≤ Fintype.card A
```

## Dependencies

- rank_lt_card
