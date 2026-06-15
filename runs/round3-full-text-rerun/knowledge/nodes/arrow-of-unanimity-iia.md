---
id: arrow-of-unanimity-iia
title: arrow_of_unanimity_iia
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.Voting.Decisive
  declarations:
    - arrow_of_unanimity_iia
uses:
  - SWF
  - Unanimity
  - IIA
  - Dictatorial
  - decisive_minimal
---

# arrow_of_unanimity_iia

## Lean type

```lean
theorem arrow_of_unanimity_iia [Fintype N] [Nonempty N] [Fintype A] (h0 : ∃ x y z : A, x ≠ y ∧ x ≠ z ∧ y ≠ z) {F : SWF N A} (h1 : SWF.Unanimity F) (h2 : SWF.IIA F) : SWF.Dictatorial F
```

## Dependencies

- SWF
- Unanimity
- IIA
- Dictatorial
- decisive_minimal
