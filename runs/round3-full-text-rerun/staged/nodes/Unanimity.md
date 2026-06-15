---
id: Unanimity
title: Unanimity
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - Unanimity
uses:
  - VotingRule
  - Profile
  - Prefers
---

# Unanimity

## Lean type

```lean
def Unanimity (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Profile
- Prefers
