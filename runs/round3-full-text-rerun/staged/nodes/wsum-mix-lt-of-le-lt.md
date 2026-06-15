---
id: wsum-mix-lt-of-le-lt
title: wsum_mix_lt_of_le_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_mix_lt_of_le_lt
uses:
  - stdSimplex.mix
  - Lottery.mix
  - wsum_mix
  - linear_comb_lt_of_le_lt
---

# wsum_mix_lt_of_le_lt

## Lean type

```lean
theorem wsum_mix_lt_of_le_lt {I : Type*} [Fintype I] (f : I → 𝕜) (x y : stdSimplex 𝕜 I) (c : 𝕜) (H1 : wsum x f ≤ c) (H2 : wsum y f < c) {t : 𝕜} (ht₀ : 0 ≤ t) (ht₁ : t ≤ 1) (Ht : t < 1) : wsum (stdSimplex.mix t ht₀ ht₁ x y) f < c
```

## Dependencies

- stdSimplex.mix
- Lottery.mix
- wsum_mix
- linear_comb_lt_of_le_lt
