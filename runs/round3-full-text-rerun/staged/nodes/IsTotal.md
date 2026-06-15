---
id: IsTotal
title: IsTotal
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - IsTotal
uses:
  - VotingRule
  - Profile
---

# IsTotal

## Lean type

```lean
def IsTotal [Fintype N] [Fintype A] (f : VotingRule N A) : Prop
```

## Dependencies

- VotingRule
- Profile
