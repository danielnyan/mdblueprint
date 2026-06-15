---
id: IsWeaklyDecisiveFor
title: IsWeaklyDecisiveFor
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - IsWeaklyDecisiveFor
uses:
  - SWF
  - Profile
  - Prefers
---

# IsWeaklyDecisiveFor

## Lean type

```lean
def IsWeaklyDecisiveFor [Fintype N] [Fintype A] (F : SWF N A) (C : Set N) (a b : A) : Prop
```

## Dependencies

- SWF
- Profile
- Prefers
