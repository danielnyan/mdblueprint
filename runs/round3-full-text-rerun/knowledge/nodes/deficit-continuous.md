---
id: deficit-continuous
title: deficit_continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - deficit_continuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - BigSimplex
  - blockSum_continuous
---

# deficit_continuous

## Lean type

```lean
lemma deficit_continuous : Continuous (deficit card)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- BigSimplex
- blockSum_continuous
