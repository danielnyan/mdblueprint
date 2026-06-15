---
id: blockSum-pushTowardsZ-pos
title: blockSum_pushTowardsZ_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - blockSum_pushTowardsZ_pos
uses:
  - BigSimplex
  - blockSum_pushTowardsZ_formula
  - blockWeight_pos
  - blockSum_nonneg
  - tPush_mem_Icc
  - deficit_nonneg
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# blockSum_pushTowardsZ_pos

## Lean type

```lean
lemma blockSum_pushTowardsZ_pos (i : I) (x : BigSimplex card) : 0 < blockSum card i (pushTowardsZ card x)
```

## Dependencies

- BigSimplex
- blockSum_pushTowardsZ_formula
- blockWeight_pos
- blockSum_nonneg
- tPush_mem_Icc
- deficit_nonneg
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- IsPositiveAffineOf.symm
- Indifferent.symm
