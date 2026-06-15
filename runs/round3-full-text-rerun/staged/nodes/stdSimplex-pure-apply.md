---
id: stdSimplex-pure-apply
title: stdSimplex.pure_apply
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - stdSimplex.pure_apply
uses:
  - stdSimplex.pure
  - Lottery.pure
---

# stdSimplex.pure_apply

## Lean type

```lean
@[simp] theorem stdSimplex.pure_apply [DecidableEq I] (i₀ i : I) : (stdSimplex.pure (𝕜
```

## Dependencies

- stdSimplex.pure
- Lottery.pure
