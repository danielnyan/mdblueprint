---
id: rank-lt-card
title: rank_lt_card
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - rank_lt_card
uses:
  - BallotPrefers
---

# rank_lt_card

## Lean type

```lean
theorem rank_lt_card [Fintype A] (r : LinearOrder A) (a : A) : rank r a < Fintype.card A
```

## Dependencies

- BallotPrefers
