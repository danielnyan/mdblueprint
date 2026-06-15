---
id: zProfile-prefers-outside
title: zProfile_prefers_outside
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.ProfileSurgery
  declarations:
    - zProfile_prefers_outside
uses:
  - Profile
  - Prefers
  - rank_lt_iff
---

# zProfile_prefers_outside

## Lean type

```lean
theorem zProfile_prefers_outside [Fintype N] [Fintype A] (P Q : Profile N A) (R : Set A) [∀ a : A, Decidable (a ∈ R)] {a b : A} (ha : a ∉ R) (hb : b ∉ R) (i : N) : Prefers (zProfile P Q R) i a b ↔ Prefers Q i a b
```

## Dependencies

- Profile
- Prefers
- rank_lt_iff
