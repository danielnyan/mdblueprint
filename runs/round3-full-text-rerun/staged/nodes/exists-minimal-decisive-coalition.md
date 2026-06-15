---
id: exists-minimal-decisive-coalition
title: exists_minimal_decisive_coalition
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - exists_minimal_decisive_coalition
uses:
  - SWF
  - Unanimity
  - exists_nonempty_decisive_of_size
  - unanimity_univ_isDecisive
  - IIA
  - Profile
  - Prefers
  - IsDecisive
  - decisive_spread
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - StrictlyPreferred.asymm
  - BallotPrefers.asymm
  - Prefers.asymm
  - iia_strict
---

# exists_minimal_decisive_coalition

## Lean type

```lean
theorem exists_minimal_decisive_coalition [Fintype N] [Nonempty N] [Fintype A] {F : SWF N A} (hU : SWF.Unanimity F) : ∃ n, Minimal (exists_nonempty_decisive_of_size F) n
```

## Dependencies

- SWF
- Unanimity
- exists_nonempty_decisive_of_size
- unanimity_univ_isDecisive
- IIA
- Profile
- Prefers
- IsDecisive
- decisive_spread
- IsPositiveAffineOf.symm
- Indifferent.symm
- StrictlyPreferred.asymm
- BallotPrefers.asymm
- Prefers.asymm
- iia_strict
