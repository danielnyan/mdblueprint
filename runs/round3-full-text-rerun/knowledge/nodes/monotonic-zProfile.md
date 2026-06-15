---
id: monotonic-zProfile
title: monotonic_zProfile
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.GibbardSatterthwaite
  declarations:
    - monotonic_zProfile
uses:
  - VotingRule
  - Monotonicity
  - Profile
  - zProfile_prefers_inside
  - zProfile_prefers_inside_outside
  - StrictlyPreferred.asymm
  - BallotPrefers.asymm
  - Prefers.asymm
  - Prefers
---

# monotonic_zProfile

## Lean type

```lean
theorem monotonic_zProfile [Fintype N] [Fintype A] (f : VotingRule N A) (hM : Monotonicity f) (P Q : Profile N A) (R : Set A) [∀ a : A, Decidable (a ∈ R)] {a : A} (haR : a ∈ R) (ha : a ∈ f P) : a ∈ f (zProfile P Q R)
```

## Dependencies

- VotingRule
- Monotonicity
- Profile
- zProfile_prefers_inside
- zProfile_prefers_inside_outside
- StrictlyPreferred.asymm
- BallotPrefers.asymm
- Prefers.asymm
- Prefers
