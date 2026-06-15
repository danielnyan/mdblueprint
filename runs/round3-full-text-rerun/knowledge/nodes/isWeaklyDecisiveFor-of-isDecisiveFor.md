---
id: isWeaklyDecisiveFor-of-isDecisiveFor
title: isWeaklyDecisiveFor_of_isDecisiveFor
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - isWeaklyDecisiveFor_of_isDecisiveFor
uses:
  - SWF
  - IsDecisiveFor
  - IsWeaklyDecisiveFor
---

# isWeaklyDecisiveFor_of_isDecisiveFor

## Lean type

```lean
theorem isWeaklyDecisiveFor_of_isDecisiveFor [Fintype N] [Fintype A] {F : SWF N A} {C : Set N} {a b : A} (h : IsDecisiveFor F C a b) : IsWeaklyDecisiveFor F C a b
```

## Dependencies

- SWF
- IsDecisiveFor
- IsWeaklyDecisiveFor
