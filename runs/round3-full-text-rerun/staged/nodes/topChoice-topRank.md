---
id: topChoice-topRank
title: topChoice_topRank
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - topChoice_topRank
uses:
  - Profile
  - TopRank
  - Prefers
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# topChoice_topRank

## Lean type

```lean
theorem topChoice_topRank [Fintype N] [Fintype A] [Nonempty A] (P : Profile N A) (i : N) : TopRank P i (topChoice P i)
```

## Dependencies

- Profile
- TopRank
- Prefers
- IsPositiveAffineOf.symm
- Indifferent.symm
