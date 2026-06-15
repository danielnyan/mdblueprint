---
id: Monotonicity
title: Monotonicity
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - Monotonicity
uses:
  - VotingRule
  - Profile
  - SimpleLift
---

# Monotonicity

## Lean type

```lean
def Monotonicity (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Profile
- SimpleLift
