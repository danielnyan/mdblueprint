---
id: blockSum-nonneg
title: blockSum_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - blockSum_nonneg
uses:
  - BigSimplex
---

# blockSum_nonneg

## Lean type

```lean
lemma blockSum_nonneg (i : I) (x : BigSimplex card) : 0 ≤ blockSum card i x
```

## Dependencies

- BigSimplex
