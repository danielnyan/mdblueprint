---
id: decisive-minimal
title: decisive_minimal
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - decisive_minimal
uses:
  - SWF
  - Unanimity
  - IIA
  - exists_nonempty_decisive_of_size
  - exists_minimal_decisive_coalition
  - decisive_contraction
---

# decisive_minimal

## Lean type

```lean
theorem decisive_minimal [Fintype N] [Nonempty N] [Fintype A] (h0 : ∃ x y z : A, x ≠ y ∧ x ≠ z ∧ y ≠ z) {F : SWF N A} (hU : SWF.Unanimity F) (hIIA : SWF.IIA F) : Minimal (exists_nonempty_decisive_of_size F) 1
```

## Dependencies

- SWF
- Unanimity
- IIA
- exists_nonempty_decisive_of_size
- exists_minimal_decisive_coalition
- decisive_contraction
