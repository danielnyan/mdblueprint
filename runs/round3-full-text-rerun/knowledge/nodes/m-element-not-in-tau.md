---
id: m-element-not-in-tau
title: m_element_not_in_tau
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - m_element_not_in_tau
uses:
  - isDoor
  - M_set
  - is_maximal_in_M_set
  - m_element_is_maximal
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# m_element_not_in_tau

## Lean type

```lean
lemma m_element_not_in_tau [Fintype T] (τ : Finset T) (D : Finset I) (i a b : I) (h_door : IST.isDoor τ D) (h_nonempty : τ.Nonempty) (ha_mem : a ∈ D) (hb_mem : b ∈ D) (hab : a ≠ b) (h_eq_mini : mini h_nonempty a = mini h_nonempty b) (h_M_nonempty : (M_set τ D i h_nonempty).Nonempty) (h_i_is : i = a ∨ i = b) : m_element τ D i h_nonempty h_M_nonempty ∉ τ
```

## Dependencies

- isDoor
- M_set
- is_maximal_in_M_set
- m_element_is_maximal
- IsPositiveAffineOf.symm
- Indifferent.symm
