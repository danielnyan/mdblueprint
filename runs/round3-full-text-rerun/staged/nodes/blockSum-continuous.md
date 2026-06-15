---
id: blockSum-continuous
title: blockSum_continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - blockSum_continuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - BigSimplex
---

# blockSum_continuous

## Lean type

```lean
lemma blockSum_continuous (i : I) : Continuous (blockSum card i)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- BigSimplex
