---
id: rank-lt-of-lt
title: rank_lt_of_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - rank_lt_of_lt
uses:
  - BallotPrefers
---

# rank_lt_of_lt

## Lean type

```lean
theorem rank_lt_of_lt [Fintype A] (r : LinearOrder A) {a b : A} (hab : BallotPrefers r a b) : rank r a < rank r b
```

## Dependencies

- BallotPrefers
