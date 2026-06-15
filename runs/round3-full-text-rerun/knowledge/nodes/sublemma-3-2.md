---
id: sublemma-3-2
title: sublemma_3_2
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - sublemma_3_2
uses:
  - isDoor
  - isDominant
  - M_set
  - is_maximal_in_M_set
  - keylemma_of_dominant
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - isRoom
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# sublemma_3_2

## Lean type

```lean
lemma sublemma_3_2 [Fintype T] (τ : Finset T) (D : Finset I) (x : T) (h_door : IST.isDoor τ D) (h_nonempty : τ.Nonempty) (h_not_mem : x ∉ τ) (a b : I) (ha : a ∈ D) (hb : b ∈ D) (hab : a ≠ b) (h_eq : mini h_nonempty a = mini h_nonempty b) : IST.isDominant (insert x τ) D ↔ (∃ i ∈ ({a, b} : Finset I), (M_set τ D i h_nonempty).Nonempty ∧ is_maximal_in_M_set τ D i h_nonempty x)
```

## Dependencies

- isDoor
- isDominant
- M_set
- is_maximal_in_M_set
- keylemma_of_dominant
- IsPositiveAffineOf.symm
- Indifferent.symm
- isRoom
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
