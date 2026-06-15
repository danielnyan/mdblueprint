---
id: vetoScore
title: vetoScore
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - vetoScore
uses:
  - VotingRule
  - pluralityScore
  - bordaScore
---

# vetoScore

## Lean type

```lean
def vetoScore (m r : Nat) : Int
```

## Dependencies

- VotingRule
- pluralityScore
- bordaScore
