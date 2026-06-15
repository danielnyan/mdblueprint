---
id: permuteVoters
title: permuteVoters
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - permuteVoters
uses:
  - Profile
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# permuteVoters

## Lean type

```lean
def permuteVoters [Fintype N] [Fintype A] (P : Profile N A) (σ : Equiv.Perm N) : Profile N A
```

## Dependencies

- Profile
- IsPositiveAffineOf.symm
- Indifferent.symm
