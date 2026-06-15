---
id: Prefers
title: Prefers
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - Prefers
uses:
  - Profile
  - BallotPrefers
---

# Prefers

## Lean type

```lean
def Prefers [Fintype N] [Fintype A] (P : Profile N A) (i : N) (a b : A) : Prop
```

## Dependencies

- Profile
- BallotPrefers
