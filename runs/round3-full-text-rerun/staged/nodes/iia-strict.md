---
id: iia-strict
title: iia_strict
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - iia_strict
uses:
  - SWF
  - IIA
  - Profile
  - Prefers
  - BallotPrefers
  - rank_injective
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - rank_lt_iff
  - rank_lt_card
  - StrictlyPreferred.asymm
  - BallotPrefers.asymm
  - Prefers.asymm
  - Unanimity
  - IsWeaklyDecisiveFor
  - IsDecisiveFor
  - strict_transitive
  - isWeaklyDecisiveFor_of_isDecisiveFor
---

# iia_strict

## Lean type

```lean
theorem iia_strict [Fintype N] [Fintype A] {F : SWF N A} (hF : SWF.IIA F) {P Q : Profile N A} {a b : A} (hab : ∀ i, Prefers P i a b ↔ Prefers Q i a b) (hba : ∀ i, Prefers P i b a ↔ Prefers Q i b a) : strict (F P) a b ↔ strict (F Q) a b
```

## Dependencies

- SWF
- IIA
- Profile
- Prefers
- BallotPrefers
- rank_injective
- IsPositiveAffineOf.symm
- Indifferent.symm
- rank_lt_iff
- rank_lt_card
- StrictlyPreferred.asymm
- BallotPrefers.asymm
- Prefers.asymm
- Unanimity
- IsWeaklyDecisiveFor
- IsDecisiveFor
- strict_transitive
- isWeaklyDecisiveFor_of_isDecisiveFor
