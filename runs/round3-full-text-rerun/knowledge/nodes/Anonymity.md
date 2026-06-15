---
id: Anonymity
title: Anonymity
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - Anonymity
uses:
  - VotingRule
  - Profile
  - permuteVoters
---

# Anonymity

## Lean type

```lean
def Anonymity (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Profile
- permuteVoters
