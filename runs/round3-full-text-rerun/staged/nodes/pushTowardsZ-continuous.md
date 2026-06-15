---
id: pushTowardsZ-continuous
title: pushTowardsZ_continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - pushTowardsZ_continuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - BigSimplex
  - tPush_continuous
---

# pushTowardsZ_continuous

## Lean type

```lean
lemma pushTowardsZ_continuous : Continuous (pushTowardsZ card)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- BigSimplex
- tPush_continuous
