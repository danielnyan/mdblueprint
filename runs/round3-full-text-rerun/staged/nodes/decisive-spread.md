---
id: decisive-spread
title: decisive_spread
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - decisive_spread
uses:
  - SWF
  - Unanimity
  - IIA
  - IsWeaklyDecisiveFor
  - IsDecisive
  - isWeaklyDecisiveFor_of_isDecisiveFor
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# decisive_spread

## Lean type

```lean
theorem decisive_spread [Fintype N] [Fintype A] {F : SWF N A} (hU : SWF.Unanimity F) (hIIA : SWF.IIA F) {C : Set N} {x y z : A} (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z) (hC : Set.Nonempty C) (h : IsWeaklyDecisiveFor F C x y) : IsDecisive F C
```

## Dependencies

- SWF
- Unanimity
- IIA
- IsWeaklyDecisiveFor
- IsDecisive
- isWeaklyDecisiveFor_of_isDecisiveFor
- IsPositiveAffineOf.symm
- Indifferent.symm
