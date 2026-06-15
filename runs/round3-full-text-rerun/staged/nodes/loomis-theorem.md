---
id: loomis-theorem
title: loomis_theorem
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - loomis_theorem
uses:
  - IsPositive
  - exists_xx_lamB0
  - exists_yy_muB0
  - loomis_value_eq
  - wsum_const
  - Profile.ext
---

# loomis_theorem

## Lean type

```lean
theorem loomis_theorem (A B : I → J → ℝ) (hB : IsPositive B) : ∃ (x : stdSimplex ℝ I) (y : stdSimplex ℝ J) (v : ℝ), (∀ j, v * xB B x j ≤ xA A x j) ∧ (∀ i, Ay A y i ≤ v * By B y i)
```

## Dependencies

- IsPositive
- exists_xx_lamB0
- exists_yy_muB0
- loomis_value_eq
- wsum_const
- Profile.ext
