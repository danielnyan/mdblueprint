---
id: stdSimplex-mix-apply
title: stdSimplex.mix_apply
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - stdSimplex.mix_apply
uses:
  - stdSimplex.mix
  - Lottery.mix
---

# stdSimplex.mix_apply

## Lean type

```lean
@[simp] theorem stdSimplex.mix_apply (α : 𝕜) (hα₀ : 0 ≤ α) (hα₁ : α ≤ 1) (x y : stdSimplex 𝕜 I) (i : I) : (stdSimplex.mix α hα₀ hα₁ x y).val i = α * x.val i + (1 - α) * y.val i
```

## Dependencies

- stdSimplex.mix
- Lottery.mix
