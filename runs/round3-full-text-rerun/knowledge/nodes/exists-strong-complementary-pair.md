---
id: exists-strong-complementary-pair
title: exists_strong_complementary_pair
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongComplementarity
  declarations:
    - exists_strong_complementary_pair
uses:
  - optimalRowStrategies
  - optimalColumnStrategies
  - exists_mixed_nash_equilibrium
  - optimal_pairs_iff_saddle_point
  - mem_optimalRowStrategies_iff_E_ge
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
  - mem_optimalColumnStrategies_iff_E_le
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - DualFeasible
  - wsum_wsum_comm
  - wsum_const
  - wsum_le_wsum
  - support_complementarity_row
  - support_complementarity_column
  - DualFeasible
  - exists_row_strict_pair
  - exists_col_strict_pair
---

# exists_strong_complementary_pair

## Lean type

```lean
theorem exists_strong_complementary_pair (A : I → Fin n → 𝕜) (b : I → 𝕜) (c : Fin n → 𝕜) (v : 𝕜) (hN_pos : (0 : 𝕜) < ((Fintype.card I + n : ℕ) : 𝕜)) {x₀ : Fin n → 𝕜} (hx₀A : ∀ i, b i ≤ ∑ j, A i j * x₀ j) (hx₀nn : ∀ j, 0 ≤ x₀ j) (hx₀_val : ∑ j, c j * x₀ j = v) {u₀ : I → 𝕜} (hu₀ : DualFeasible A c u₀) (hu₀_val : ∑ i, u₀ i * b i = v) : ∃ (x : Fin n → 𝕜) (u : I → 𝕜), (∀ i, b i ≤ ∑ j, A i j * x j) ∧ (∀ j, 0 ≤ x j) ∧ DualFeasible A c u ∧ (∑ j, c j * x j = v) ∧ (∑ i, u i * b i = v) ∧ (∀ i, 0 < (∑ j, A i j * x j - b i) + u i) ∧ (∀ j, 0 < x j + (c j - ∑ i, u i * A i j))
```

## Dependencies

- optimalRowStrategies
- optimalColumnStrategies
- exists_mixed_nash_equilibrium
- optimal_pairs_iff_saddle_point
- mem_optimalRowStrategies_iff_E_ge
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
- mem_optimalColumnStrategies_iff_E_le
- IsPositiveAffineOf.symm
- Indifferent.symm
- DualFeasible
- wsum_wsum_comm
- wsum_const
- wsum_le_wsum
- support_complementarity_row
- support_complementarity_column
- DualFeasible
- exists_row_strict_pair
- exists_col_strict_pair
