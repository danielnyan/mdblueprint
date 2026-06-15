---
id: wsum-pure-apply
title: wsum_pure_apply
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_pure_apply
uses:
  - stdSimplex.pure
  - Lottery.pure
---

# wsum_pure_apply

## Lean type

```lean
@[simp] theorem wsum_pure_apply [DecidableEq I] (i₀ : I) (f : I → 𝕜) : wsum (stdSimplex.pure (𝕜
```

## Dependencies

- stdSimplex.pure
- Lottery.pure
