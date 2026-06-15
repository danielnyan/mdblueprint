---
id: tPush-continuous
title: tPush_continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - tPush_continuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - deficit_continuous
  - deficit_nonneg
---

# tPush_continuous

## Lean type

```lean
lemma tPush_continuous : Continuous (tPush card)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- deficit_continuous
- deficit_nonneg
