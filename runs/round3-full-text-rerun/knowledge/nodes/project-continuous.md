---
id: project-continuous
title: project_continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - project_continuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - BigSimplex
  - pushTowardsZ_continuous
  - blockSum_pushTowardsZ_pos
---

# project_continuous

## Lean type

```lean
lemma project_continuous : Continuous (project_to_product card)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- BigSimplex
- pushTowardsZ_continuous
- blockSum_pushTowardsZ_pos
