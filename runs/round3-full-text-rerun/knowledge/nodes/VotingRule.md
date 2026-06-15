---
id: VotingRule
title: VotingRule
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - VotingRule
uses:
  - Profile
---

# VotingRule

## Lean type

```lean
abbrev VotingRule (N A : Type*) [Fintype N] [Fintype A]
```

## Dependencies

- Profile
