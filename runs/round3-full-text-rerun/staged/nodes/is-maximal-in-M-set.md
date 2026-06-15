---
id: is-maximal-in-M-set
title: is_maximal_in_M_set
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - is_maximal_in_M_set
uses:
  - M_set
  - toFinset
---

# is_maximal_in_M_set

## Lean type

```lean
def is_maximal_in_M_set (τ : Finset T) (D : Finset I) (i : I) (h_nonempty : τ.Nonempty) (x : T) : Prop
```

## Dependencies

- M_set
- toFinset
