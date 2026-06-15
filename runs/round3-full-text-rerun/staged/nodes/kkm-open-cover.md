---
id: kkm-open-cover
title: kkm_open_cover
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.KKM
  declarations:
    - kkm_open_cover
uses:
  - simplexFaceOpp
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - IsKKMCover
  - mem_iUnion
  - kkm_closed_cover
---

# kkm_open_cover

## Lean type

```lean
theorem kkm_open_cover (hn : 0 < n) (U : Fin n → Set (Fin n → ℝ)) (hopen : ∀ i, IsOpen (U i)) (hface : ∀ i, simplexFaceOpp i ⊆ (U i)ᶜ) (hcover : stdSimplex ℝ (Fin n) ⊆ ⋃ i, U i) : ∃ x ∈ stdSimplex ℝ (Fin n), ∀ i, x ∈ U i
```

## Dependencies

- simplexFaceOpp
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- IsKKMCover
- mem_iUnion
- kkm_closed_cover
