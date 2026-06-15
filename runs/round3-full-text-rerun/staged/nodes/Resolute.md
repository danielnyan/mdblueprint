---
id: Resolute
title: Resolute
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - Resolute
uses:
  - VotingRule
  - Profile
---

# Resolute

## Lean type

```lean
def Resolute [Fintype N] [Fintype A] (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Profile
