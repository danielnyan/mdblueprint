---
id: scoringRule-isTotal
title: scoringRule_isTotal
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - scoringRule_isTotal
uses:
  - IsTotal
  - scoringWinners_nonempty
---

# scoringRule_isTotal

## Lean type

```lean
theorem scoringRule_isTotal (score : Nat → Nat → Int) [Fintype N] [Fintype A] [Nonempty A] : IsTotal (N
```

## Dependencies

- IsTotal
- scoringWinners_nonempty
