---
id: Profile-ext
title: Profile.ext
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - Profile.ext
uses:
  - Profile
---

# Profile.ext

## Lean type

```lean
@[ext] theorem Profile.ext [Fintype N] [Fintype A] {P Q : Profile N A} (h : ∀ i : N, P.pref i = Q.pref i) : P = Q
```

## Dependencies

- Profile
