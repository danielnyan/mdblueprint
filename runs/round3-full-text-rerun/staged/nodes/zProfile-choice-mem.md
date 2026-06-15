---
id: zProfile-choice-mem
title: zProfile_choice_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.GibbardSatterthwaite
  declarations:
    - zProfile_choice_mem
uses:
  - VotingRule
  - Unanimity
  - Monotonicity
  - Profile
  - zProfile_prefers_inside_outside
  - zProfile_prefers_inside
  - StrictlyPreferred.asymm
  - BallotPrefers.asymm
  - Prefers.asymm
  - Prefers
  - IsTotal
  - Resolute
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - SWF
  - BallotPrefers.total_of_ne
  - Prefers.total_of_ne
  - IIA
---

# zProfile_choice_mem

## Lean type

```lean
theorem zProfile_choice_mem [Fintype N] [Nonempty N] [Fintype A] (f : VotingRule N A) (hU : Unanimity f) (_hM : Monotonicity f) (P Q : Profile N A) (R : Set A) [∀ a : A, Decidable (a ∈ R)] (hR : R.Nonempty) {a : A} (ha : a ∈ f (zProfile P Q R)) : a ∈ R
```

## Dependencies

- VotingRule
- Unanimity
- Monotonicity
- Profile
- zProfile_prefers_inside_outside
- zProfile_prefers_inside
- StrictlyPreferred.asymm
- BallotPrefers.asymm
- Prefers.asymm
- Prefers
- IsTotal
- Resolute
- IsPositiveAffineOf.symm
- Indifferent.symm
- SWF
- BallotPrefers.total_of_ne
- Prefers.total_of_ne
- IIA
