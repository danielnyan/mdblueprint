---
id: veto-isTotal
title: veto_isTotal
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - veto_isTotal
uses:
  - IsTotal
  - scoringRule_isTotal
  - vetoScore
  - Profile
  - MajorityPrefers
  - VotingRule
---

# veto_isTotal

## Lean type

```lean
theorem veto_isTotal [Fintype N] [Fintype A] [Nonempty A] : IsTotal (N
```

## Dependencies

- IsTotal
- scoringRule_isTotal
- vetoScore
- Profile
- MajorityPrefers
- VotingRule
