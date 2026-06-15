---
id: wsum-mix-gt-of-ge-gt
title: wsum_mix_gt_of_ge_gt
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_mix_gt_of_ge_gt
uses:
  - stdSimplex.mix
  - Lottery.mix
  - wsum_mix
  - linear_comb_gt_of_ge_gt
---

# wsum_mix_gt_of_ge_gt

## Lean type

```lean
theorem wsum_mix_gt_of_ge_gt {I : Type*} [Fintype I] (f : I → 𝕜) (x y : stdSimplex 𝕜 I) (c : 𝕜) (H1 : c ≤ wsum x f) (H2 : c < wsum y f) {t : 𝕜} (ht₀ : 0 ≤ t) (ht₁ : t ≤ 1) (Ht : t < 1) : c < wsum (stdSimplex.mix t ht₀ ht₁ x y) f
```

## Dependencies

- stdSimplex.mix
- Lottery.mix
- wsum_mix
- linear_comb_gt_of_ge_gt
