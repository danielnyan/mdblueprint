---
id: BottomRank
title: BottomRank
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - BottomRank
uses:
  - Profile
  - Prefers
---

# BottomRank

## Lean type

```lean
def BottomRank [Fintype N] [Fintype A] (P : Profile N A) (i : N) (a : A) : Prop
```

## Dependencies

- Profile
- Prefers
