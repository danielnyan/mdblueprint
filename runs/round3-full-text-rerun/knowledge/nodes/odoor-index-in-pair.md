---
id: odoor-index-in-pair
title: odoor_index_in_pair
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - odoor_index_in_pair
uses:
  - isDoor
  - isDominant
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - keylemma_of_dominant
---

# odoor_index_in_pair

## Lean type

```lean
lemma odoor_index_in_pair [Fintype T] (τ : Finset T) (D : Finset I) (C : Finset I) (a b j : I) (_h_door : IST.isDoor τ D) (h_nonempty : τ.Nonempty) (ha_mem : a ∈ D) (hb_mem : b ∈ D) (hab : a ≠ b) (h_eq_mini : mini h_nonempty a = mini h_nonempty b) (h_dom : IST.isDominant τ C) (h_room_card : C.card = τ.card) (_hj_not_mem : j ∉ C) (hc_eq : D = insert j C) : j ∈ ({a, b} : Finset I)
```

## Dependencies

- isDoor
- isDominant
- IsPositiveAffineOf.symm
- Indifferent.symm
- keylemma_of_dominant
