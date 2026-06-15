---
id: rotateBundles-isAllocation
title: rotateBundles_isAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.EnvyCycle
  declarations:
    - rotateBundles_isAllocation
uses:
  - Allocation
  - rotateBundles_not_mem
  - rotateBundles_mem
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - Profile.ext
  - mem_biUnion
---

# rotateBundles_isAllocation

## Lean type

```lean
lemma rotateBundles_isAllocation [Fintype N] {allGoods : Finset G} {A : Allocation N G} (hA : IsAllocation allGoods A) (l : List N) (hnd : l.Nodup) : IsAllocation allGoods (rotateBundles A l)
```

## Dependencies

- Allocation
- rotateBundles_not_mem
- rotateBundles_mem
- IsPositiveAffineOf.symm
- Indifferent.symm
- Profile.ext
- mem_biUnion
