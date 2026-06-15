---
id: position-eq-rank-succ
title: position_eq_rank_succ
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - position_eq_rank_succ
uses:
---

# position_eq_rank_succ

## Lean type

```lean
theorem position_eq_rank_succ [Fintype A] (r : LinearOrder A) (a : A) : position r a = rank r a + 1
```

## Dependencies

- none
