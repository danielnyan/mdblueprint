---
id: Dictatorial
title: Dictatorial
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - Dictatorial
uses:
  - VotingRule
  - Profile
---

# Dictatorial

## Lean type

```lean
def Dictatorial [Nonempty A] (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Profile
