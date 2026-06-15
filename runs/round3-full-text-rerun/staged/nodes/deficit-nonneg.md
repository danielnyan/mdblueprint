---
id: deficit-nonneg
title: deficit_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - deficit_nonneg
uses:
  - BigSimplex
---

# deficit_nonneg

## Lean type

```lean
lemma deficit_nonneg (x : BigSimplex card) : 0 ≤ deficit card x
```

## Dependencies

- BigSimplex
