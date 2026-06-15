---
id: MatrixGame-antisymmetric-exists-optimal-strategy
title: MatrixGame.antisymmetric_exists_optimal_strategy
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.Antisymmetric
  declarations:
    - MatrixGame.antisymmetric_exists_optimal_strategy
uses:
  - IsAntisymmetric
  - optimalRowStrategies
  - optimalColumnStrategies
  - exists_mixed_nash_equilibrium
  - optimal_pairs_iff_saddle_point
  - mem_optimalColumnStrategies_iff_E_le
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
  - MatrixGame.antisymmetric_value_zero
---

# MatrixGame.antisymmetric_exists_optimal_strategy

## Lean type

```lean
theorem MatrixGame.antisymmetric_exists_optimal_strategy {B : I → I → ℝ} (hB : IsAntisymmetric B) : ∃ y : stdSimplex ℝ I, ∀ i, ∑ j, B i j * y.val j ≤ 0
```

## Dependencies

- IsAntisymmetric
- optimalRowStrategies
- optimalColumnStrategies
- exists_mixed_nash_equilibrium
- optimal_pairs_iff_saddle_point
- mem_optimalColumnStrategies_iff_E_le
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
- MatrixGame.antisymmetric_value_zero
