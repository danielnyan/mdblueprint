---
id: plurality-isTotal
title: plurality_isTotal
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - plurality_isTotal
uses:
  - IsTotal
  - scoringRule_isTotal
  - pluralityScore
---

# plurality_isTotal

## Lean type

```lean
theorem plurality_isTotal [Fintype N] [Fintype A] [Nonempty A] : IsTotal (N
```

## Dependencies

- IsTotal
- scoringRule_isTotal
- pluralityScore
