---
id: strom-value-continuous
title: strom_value_continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Existence
  declarations:
    - strom_value_continuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - cdfRealContinuous
  - simplexFaceOpp
  - strom_piece_empty_iff
  - strom_piece_partition
  - Profile.ext
  - mem_iUnion
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - mem_biUnion
  - Allocation
  - IsEnvyFree
  - MeasureValuation
  - kkm_open_cover
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# strom_value_continuous

## Lean type

```lean
lemma strom_value_continuous (j i : Fin n) : Continuous (fun x : Fin n → ℝ => strom_value n μ x j i)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- cdfRealContinuous
- simplexFaceOpp
- strom_piece_empty_iff
- strom_piece_partition
- Profile.ext
- mem_iUnion
- IsPositiveAffineOf.symm
- Indifferent.symm
- mem_biUnion
- Allocation
- IsEnvyFree
- MeasureValuation
- kkm_open_cover
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
