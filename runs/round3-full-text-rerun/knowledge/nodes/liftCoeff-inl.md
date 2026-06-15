---
id: liftCoeff-inl
title: liftCoeff_inl
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - liftCoeff_inl
uses:
  - ZeroRows
  - liftCoeff
---

# liftCoeff_inl

## Lean type

```lean
theorem liftCoeff_inl (A : I → Fin (n+1) → 𝕜) (k : ZeroRows A) (i : I) : liftCoeff A (Sum.inl k) i = if k.val = i then 1 else 0
```

## Dependencies

- ZeroRows
- liftCoeff
