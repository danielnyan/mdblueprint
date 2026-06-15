---
id: Neutrality
title: Neutrality
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - Neutrality
uses:
  - VotingRule
  - Profile
---

# Neutrality

## Lean type

```lean
def Neutrality (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Profile
