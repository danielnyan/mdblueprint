---
id: wsum-nonneg
title: wsum_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_nonneg
uses:
  - wsum_const
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - wsum_le_wsum
---

# wsum_nonneg

## Lean type

```lean
theorem wsum_nonneg (x : stdSimplex 𝕜 I) {f : I → 𝕜} (h : ∀ i, 0 ≤ f i) : 0 ≤ wsum x f
```

## Dependencies

- wsum_const
- IsPositiveAffineOf.symm
- Indifferent.symm
- wsum_le_wsum
