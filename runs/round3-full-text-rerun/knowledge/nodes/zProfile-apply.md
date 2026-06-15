---
id: zProfile-apply
title: zProfile_apply
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.ProfileSurgery
  declarations:
    - zProfile_apply
uses:
  - Profile
---

# zProfile_apply

## Lean type

```lean
@[simp] theorem zProfile_apply [Fintype N] [Fintype A] (P Q : Profile N A) (R : Set A) [∀ a : A, Decidable (a ∈ R)] (i : N) : (zProfile P Q R).pref i = zBallot (P.pref i) (Q.pref i) R
```

## Dependencies

- Profile
