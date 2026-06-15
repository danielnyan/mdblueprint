---
id: wsum-mix
title: wsum_mix
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_mix
uses:
  - stdSimplex.mix
  - Lottery.mix
---

# wsum_mix

## Lean type

```lean
theorem wsum_mix (α : 𝕜) (hα₀ : 0 ≤ α) (hα₁ : α ≤ 1) (x y : stdSimplex 𝕜 I) (f : I → 𝕜) : wsum (stdSimplex.mix α hα₀ hα₁ x y) f = α * wsum x f + (1 - α) * wsum y f
```

## Dependencies

- stdSimplex.mix
- Lottery.mix
