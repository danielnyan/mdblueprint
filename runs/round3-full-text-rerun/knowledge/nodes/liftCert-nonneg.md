---
id: liftCert-nonneg
title: liftCert_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - liftCert_nonneg
uses:
  - FMRowIndex
  - liftCert
  - liftCoeff_inl
  - liftCoeff_inr
  - liftCoeff
  - ZeroRows
  - PosRows
  - NegRows
  - fmA
  - fmB
---

# liftCert_nonneg

## Lean type

```lean
theorem liftCert_nonneg (A : I → Fin (n+1) → 𝕜) {u' : FMRowIndex A → 𝕜} (hu' : ∀ idx, 0 ≤ u' idx) (i : I) : 0 ≤ liftCert A u' i
```

## Dependencies

- FMRowIndex
- liftCert
- liftCoeff_inl
- liftCoeff_inr
- liftCoeff
- ZeroRows
- PosRows
- NegRows
- fmA
- fmB
