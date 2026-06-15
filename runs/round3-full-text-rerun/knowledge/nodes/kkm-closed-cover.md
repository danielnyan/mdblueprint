---
id: kkm-closed-cover
title: kkm_closed_cover
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.KKM
  declarations:
    - kkm_closed_cover
uses:
  - IsKKMCover
  - mem_iUnion
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - Brouwer
---

# kkm_closed_cover

## Lean type

```lean
theorem kkm_closed_cover (hn : 0 < n) (F : Fin n → Set (Fin n → ℝ)) (hclosed : ∀ i, IsClosed (F i)) (hkkm : IsKKMCover F) : ∃ x ∈ stdSimplex ℝ (Fin n), ∀ i, x ∈ F i
```

## Dependencies

- IsKKMCover
- mem_iUnion
- IsPositiveAffineOf.symm
- Indifferent.symm
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- Brouwer
