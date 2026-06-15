---
id: MatrixGame-antisymmetric-value-zero
title: MatrixGame.antisymmetric_value_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Antisymmetric
  declarations:
    - MatrixGame.antisymmetric_value_zero
uses:
  - IsAntisymmetric
  - optimalRowStrategies
  - optimalColumnStrategies
  - exists_mixed_nash_equilibrium
  - optimal_pairs_iff_saddle_point
  - mem_optimalRowStrategies_iff_E_ge
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
  - mem_optimalColumnStrategies_iff_E_le
---

# MatrixGame.antisymmetric_value_zero

## Lean type

```lean
theorem MatrixGame.antisymmetric_value_zero {B : I → I → ℝ} (hB : IsAntisymmetric B) : (⟨B⟩ : MatrixGame I I ℝ).value = 0
```

## Dependencies

- IsAntisymmetric
- optimalRowStrategies
- optimalColumnStrategies
- exists_mixed_nash_equilibrium
- optimal_pairs_iff_saddle_point
- mem_optimalRowStrategies_iff_E_ge
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
- mem_optimalColumnStrategies_iff_E_le
