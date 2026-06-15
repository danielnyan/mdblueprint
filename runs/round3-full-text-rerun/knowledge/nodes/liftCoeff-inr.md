---
id: liftCoeff-inr
title: liftCoeff_inr
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - liftCoeff_inr
uses:
  - PosRows
  - NegRows
  - liftCoeff
---

# liftCoeff_inr

## Lean type

```lean
theorem liftCoeff_inr (A : I → Fin (n+1) → 𝕜) (p : PosRows A) (q : NegRows A) (i : I) : liftCoeff A (Sum.inr (p, q)) i = (if p.val = i then -A q.val (Fin.last n) else 0) + (if q.val = i then A p.val (Fin.last n) else 0)
```

## Dependencies

- PosRows
- NegRows
- liftCoeff
