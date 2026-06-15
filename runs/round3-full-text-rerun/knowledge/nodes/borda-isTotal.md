---
id: borda-isTotal
title: borda_isTotal
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - borda_isTotal
uses:
  - IsTotal
  - scoringRule_isTotal
  - bordaScore
---

# borda_isTotal

## Lean type

```lean
theorem borda_isTotal [Fintype N] [Fintype A] [Nonempty A] : IsTotal (N
```

## Dependencies

- IsTotal
- scoringRule_isTotal
- bordaScore
