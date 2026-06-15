---
id: decisive-contraction
title: decisive_contraction
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - decisive_contraction
uses:
  - SWF
  - IsDecisive
  - Unanimity
  - IIA
  - Profile.ext
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# decisive_contraction

## Lean type

```lean
theorem decisive_contraction [Fintype N] [Fintype A] {F : SWF N A} (h0 : ∃ x y z : A, x ≠ y ∧ x ≠ z ∧ y ≠ z) {C : Set N} (hCdec : IsDecisive F C) (hCcard : 2 ≤ C.ncard) (hU : SWF.Unanimity F) (hIIA : SWF.IIA F) : ∃ S : Set N, S.Nonempty ∧ S < C ∧ IsDecisive F S
```

## Dependencies

- SWF
- IsDecisive
- Unanimity
- IIA
- Profile.ext
- IsPositiveAffineOf.symm
- Indifferent.symm
