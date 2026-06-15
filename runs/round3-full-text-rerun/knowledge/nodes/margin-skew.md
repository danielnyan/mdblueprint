---
id: margin-skew
title: margin_skew
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.VotingRules
  declarations:
    - margin_skew
uses:
  - Profile
---

# margin_skew

## Lean type

```lean
theorem margin_skew [Fintype N] [Fintype A] (P : Profile N A) (a b : A) : margin P a b = -margin P b a
```

## Dependencies

- Profile
