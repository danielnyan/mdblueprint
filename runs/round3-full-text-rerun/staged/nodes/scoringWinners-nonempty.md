---
id: scoringWinners-nonempty
title: scoringWinners_nonempty
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - scoringWinners_nonempty
uses:
  - Profile
---

# scoringWinners_nonempty

## Lean type

```lean
theorem scoringWinners_nonempty [Fintype N] [Fintype A] [Nonempty A] (P : Profile N A) (score : Nat → Int) : (scoringWinners P score).Nonempty
```

## Dependencies

- Profile
