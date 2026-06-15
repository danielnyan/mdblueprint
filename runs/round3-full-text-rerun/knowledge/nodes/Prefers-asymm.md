---
id: Prefers-asymm
title: Prefers.asymm
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - Prefers.asymm
uses:
  - Profile
  - Prefers
  - StrictlyPreferred.asymm
  - BallotPrefers.asymm
  - BallotPrefers
---

# Prefers.asymm

## Lean type

```lean
theorem Prefers.asymm [Fintype N] [Fintype A] (P : Profile N A) (i : N) {a b : A} : Prefers P i a b → ¬ Prefers P i b a
```

## Dependencies

- Profile
- Prefers
- StrictlyPreferred.asymm
- BallotPrefers.asymm
- BallotPrefers
