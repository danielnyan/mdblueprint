---
id: unanimous-strict-pref-not-chosen
title: unanimous_strict_pref_not_chosen
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.GibbardSatterthwaite
  declarations:
    - unanimous_strict_pref_not_chosen
uses:
  - VotingRule
  - Unanimity
  - Monotonicity
  - Profile
  - Prefers
---

# unanimous_strict_pref_not_chosen

## Lean type

```lean
theorem unanimous_strict_pref_not_chosen [Fintype N] [Nonempty N] [Fintype A] (f : VotingRule N A) (hU : Unanimity f) (_hM : Monotonicity f) (P : Profile N A) {a b : A} (hab : ∀ i : N, Prefers P i a b) : b ∉ f P
```

## Dependencies

- VotingRule
- Unanimity
- Monotonicity
- Profile
- Prefers
