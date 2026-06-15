---
id: IsDecisiveFor
title: IsDecisiveFor
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - IsDecisiveFor
uses:
  - SWF
  - Profile
  - Prefers
---

# IsDecisiveFor

## Lean type

```lean
def IsDecisiveFor [Fintype N] [Fintype A] (F : SWF N A) (C : Set N) (a b : A) : Prop
```

## Dependencies

- SWF
- Profile
- Prefers
