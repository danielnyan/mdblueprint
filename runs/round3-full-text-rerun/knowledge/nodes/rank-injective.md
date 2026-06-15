---
id: rank-injective
title: rank_injective
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - rank_injective
uses:
  - BallotPrefers.total_of_ne
  - Prefers.total_of_ne
  - BallotPrefers
  - rank_lt_of_lt
  - Profile
  - Prefers
---

# rank_injective

## Lean type

```lean
theorem rank_injective [Fintype A] (r : LinearOrder A) : Function.Injective (rank r)
```

## Dependencies

- BallotPrefers.total_of_ne
- Prefers.total_of_ne
- BallotPrefers
- rank_lt_of_lt
- Profile
- Prefers
