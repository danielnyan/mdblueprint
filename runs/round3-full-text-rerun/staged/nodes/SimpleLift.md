---
id: SimpleLift
title: SimpleLift
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Basic
  declarations:
    - SimpleLift
uses:
  - Profile
  - Prefers
---

# SimpleLift

## Lean type

```lean
def SimpleLift (Q P : Profile N A) (a : A) : Prop
```

## Dependencies

- Profile
- Prefers
