---
id: IsDecisive
title: IsDecisive
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - IsDecisive
uses:
  - SWF
  - IsDecisiveFor
---

# IsDecisive

## Lean type

```lean
def IsDecisive [Fintype N] [Fintype A] (F : SWF N A) (C : Set N) : Prop
```

## Dependencies

- SWF
- IsDecisiveFor
