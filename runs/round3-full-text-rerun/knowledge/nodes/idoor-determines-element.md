---
id: idoor-determines-element
title: idoor_determines_element
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - idoor_determines_element
uses:
  - isDoor
  - M_set
  - isRoom
  - isDominant
  - is_maximal_in_M_set
  - sublemma_3_2
  - maximal_element_unique
---

# idoor_determines_element

## Lean type

```lean
lemma idoor_determines_element [Fintype T] (τ : Finset T) (D : Finset I) (a b : I) (h_door : IST.isDoor τ D) (h_nonempty : τ.Nonempty) (ha_mem : a ∈ D) (hb_mem : b ∈ D) (hab : a ≠ b) (h_eq_mini : mini h_nonempty a = mini h_nonempty b) (h_Ma_nonempty : (M_set τ D a h_nonempty).Nonempty) (h_Mb_nonempty : (M_set τ D b h_nonempty).Nonempty) (x : T) (h_room : IST.isRoom (insert x τ) D) (hx_not_mem : x ∉ τ) : x = m_element τ D a h_nonempty h_Ma_nonempty ∨ x = m_element τ D b h_nonempty h_Mb_nonempty
```

## Dependencies

- isDoor
- M_set
- isRoom
- isDominant
- is_maximal_in_M_set
- sublemma_3_2
- maximal_element_unique
