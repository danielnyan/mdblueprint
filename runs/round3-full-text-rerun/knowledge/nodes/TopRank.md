---
id: TopRank
title: TopRank
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - TopRank
uses:
  - Profile
  - Prefers
---

# TopRank

## Lean type

```lean
def TopRank [Fintype N] [Fintype A] (P : Profile N A) (i : N) (a : A) : Prop
```

## Dependencies

- Profile
- Prefers
