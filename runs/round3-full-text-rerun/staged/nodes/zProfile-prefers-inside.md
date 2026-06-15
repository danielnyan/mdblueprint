---
id: zProfile-prefers-inside
title: zProfile_prefers_inside
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.ProfileSurgery
  declarations:
    - zProfile_prefers_inside
uses:
  - Profile
  - Prefers
  - rank_lt_iff
---

# zProfile_prefers_inside

## Lean type

```lean
theorem zProfile_prefers_inside [Fintype N] [Fintype A] (P Q : Profile N A) (R : Set A) [∀ a : A, Decidable (a ∈ R)] {a b : A} (ha : a ∈ R) (hb : b ∈ R) (i : N) : Prefers (zProfile P Q R) i a b ↔ Prefers P i a b
```

## Dependencies

- Profile
- Prefers
- rank_lt_iff
