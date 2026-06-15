---
id: margin-self
title: margin_self
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - margin_self
uses:
  - Profile
  - Prefers
---

# margin_self

## Lean type

```lean
theorem margin_self [Fintype N] [Fintype A] (P : Profile N A) (a : A) : margin P a a = 0
```

## Dependencies

- Profile
- Prefers
