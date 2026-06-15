---
id: blockSum-pushTowardsZ-formula
title: blockSum_pushTowardsZ_formula
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - blockSum_pushTowardsZ_formula
uses:
  - BigSimplex
---

# blockSum_pushTowardsZ_formula

## Lean type

```lean
lemma blockSum_pushTowardsZ_formula (i : I) (x : BigSimplex card) : blockSum card i (pushTowardsZ card x) = (1 - tPush card x) * blockSum card i x + (tPush card x) * blockWeight card i
```

## Dependencies

- BigSimplex
