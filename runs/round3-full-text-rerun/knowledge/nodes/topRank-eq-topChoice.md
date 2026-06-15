---
id: topRank-eq-topChoice
title: topRank_eq_topChoice
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - topRank_eq_topChoice
uses:
  - Profile
  - TopRank
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - topChoice_topRank
---

# topRank_eq_topChoice

## Lean type

```lean
theorem topRank_eq_topChoice [Fintype N] [Fintype A] [Nonempty A] (P : Profile N A) (i : N) (a : A) (ha : TopRank P i a) : a = topChoice P i
```

## Dependencies

- Profile
- TopRank
- IsPositiveAffineOf.symm
- Indifferent.symm
- topChoice_topRank
