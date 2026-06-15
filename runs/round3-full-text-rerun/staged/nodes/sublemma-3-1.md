---
id: sublemma-3-1
title: sublemma_3_1
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - sublemma_3_1
uses:
  - isDoor
  - isDominant
  - M_set
  - keylemma_of_dominant
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - injOn_sdiff
  - Profile.ext
---

# sublemma_3_1

## Lean type

```lean
lemma sublemma_3_1 [Fintype T] (τ : Finset T) (D : Finset I) (h_door : IST.isDoor τ D) (h_nonempty : τ.Nonempty) : ∀ i ∈ D, (IST.isDominant τ (D.erase i) ↔ (∃ a b, a ∈ D ∧ b ∈ D ∧ a ≠ b ∧ mini h_nonempty a = mini h_nonempty b ∧ (i = a ∨ i = b) ∧ M_set τ D i h_nonempty = ∅))
```

## Dependencies

- isDoor
- isDominant
- M_set
- keylemma_of_dominant
- IsPositiveAffineOf.symm
- Indifferent.symm
- injOn_sdiff
- Profile.ext
