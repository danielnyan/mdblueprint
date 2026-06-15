---
id: maximal-element-unique
title: maximal_element_unique
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - maximal_element_unique
uses:
  - M_set
  - is_maximal_in_M_set
  - m_element_is_maximal
---

# maximal_element_unique

## Lean type

```lean
lemma maximal_element_unique [Fintype T] (τ : Finset T) (D : Finset I) (i : I) (h_nonempty : τ.Nonempty) (h_M_nonempty : (M_set τ D i h_nonempty).Nonempty) (x : T) (h_x_max : is_maximal_in_M_set τ D i h_nonempty x) : x = m_element τ D i h_nonempty h_M_nonempty
```

## Dependencies

- M_set
- is_maximal_in_M_set
- m_element_is_maximal
