---
id: rank-lt-iff
title: rank_lt_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - rank_lt_iff
uses:
  - BallotPrefers
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - rank_lt_of_lt
---

# rank_lt_iff

## Lean type

```lean
theorem rank_lt_iff [Fintype A] (r : LinearOrder A) {a b : A} : rank r a < rank r b ↔ BallotPrefers r a b
```

## Dependencies

- BallotPrefers
- IsPositiveAffineOf.symm
- Indifferent.symm
- rank_lt_of_lt
