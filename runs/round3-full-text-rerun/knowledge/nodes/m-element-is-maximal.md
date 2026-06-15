---
id: m-element-is-maximal
title: m_element_is_maximal
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - m_element_is_maximal
uses:
  - M_set
  - is_maximal_in_M_set
  - toFinset
---

# m_element_is_maximal

## Lean type

```lean
theorem m_element_is_maximal [Fintype T] (τ : Finset T) (D : Finset I) (i : I) (h_nonempty : τ.Nonempty) (h : (M_set τ D i h_nonempty).Nonempty) : is_maximal_in_M_set τ D i h_nonempty (m_element τ D i h_nonempty h)
```

## Dependencies

- M_set
- is_maximal_in_M_set
- toFinset
