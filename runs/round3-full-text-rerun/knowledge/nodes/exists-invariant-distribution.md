---
id: exists-invariant-distribution
title: exists_invariant_distribution
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.StochasticMatrix
  declarations:
    - exists_invariant_distribution
uses:
  - optimalRowStrategies
  - optimalColumnStrategies
  - exists_mixed_nash_equilibrium
  - optimal_pairs_iff_saddle_point
  - mem_optimalRowStrategies_iff_E_ge
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
  - total_mass_preserved
---

# exists_invariant_distribution

## Lean type

```lean
theorem exists_invariant_distribution (A : I → I → ℝ) (hA : IsStochasticMatrix A) : ∃ x : stdSimplex ℝ I, ∀ j, ∑ i, x.val i * A i j = x.val j
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
- total_mass_preserved
