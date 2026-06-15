---
id: strom-piece-partition
title: strom_piece_partition
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Existence
  declarations:
    - strom_piece_partition
uses:
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - Profile.ext
  - mem_iUnion
---

# strom_piece_partition

## Lean type

```lean
lemma strom_piece_partition (x : Fin n → ℝ) (hx : x ∈ stdSimplex ℝ (Fin n)) : (∀ i, MeasurableSet (strom_piece n x i)) ∧ (∀ i j : Fin n, i ≠ j → Disjoint (strom_piece n x i) (strom_piece n x j)) ∧ (⋃ i, strom_piece n x i = Set.Ico 0 1)
```

## Dependencies

- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- Profile.ext
- mem_iUnion
