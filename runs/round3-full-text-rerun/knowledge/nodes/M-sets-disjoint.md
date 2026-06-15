---
id: M-sets-disjoint
title: M_sets_disjoint
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - M_sets_disjoint
uses:
  - isDoor
  - M_set
  - Profile.ext
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# M_sets_disjoint

## Lean type

```lean
lemma M_sets_disjoint [Fintype T] (τ : Finset T) (D : Finset I) (a b : I) (h_nonempty : τ.Nonempty) (h_door : IST.isDoor τ D) (ha : a ∈ D) (hb : b ∈ D) (hab : a ≠ b) (h_eq : mini h_nonempty a = mini h_nonempty b) : M_set τ D a h_nonempty ∩ M_set τ D b h_nonempty = ∅
```

## Dependencies

- isDoor
- M_set
- Profile.ext
- IsPositiveAffineOf.symm
- Indifferent.symm
