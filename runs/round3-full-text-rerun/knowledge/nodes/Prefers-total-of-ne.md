---
id: Prefers-total-of-ne
title: Prefers.total_of_ne
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - Prefers.total_of_ne
uses:
  - Profile
  - Prefers
  - BallotPrefers.total_of_ne
  - BallotPrefers
---

# Prefers.total_of_ne

## Lean type

```lean
theorem Prefers.total_of_ne [Fintype N] [Fintype A] (P : Profile N A) (i : N) {a b : A} (hne : a ≠ b) : Prefers P i a b ∨ Prefers P i b a
```

## Dependencies

- Profile
- Prefers
- BallotPrefers.total_of_ne
- BallotPrefers
