---
id: optimal-pairs-iff-saddle-point
title: optimal_pairs_iff_saddle_point
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - optimal_pairs_iff_saddle_point
uses:
  - optimalRowStrategies
  - optimalColumnStrategies
  - IsSaddlePoint
  - mem_optimalRowStrategies_iff_E_ge
  - mem_optimalColumnStrategies_iff_E_le
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
  - lamB.aux.bddAbove
  - lam.aux.bddAbove
  - value_eq_minimax
  - muB.aux.bddBelow
  - mu.aux.bddBelow
  - wsum_wsum_comm
---

# optimal_pairs_iff_saddle_point

## Lean type

```lean
theorem optimal_pairs_iff_saddle_point (xx : stdSimplex ℝ I) (yy : stdSimplex ℝ J) : (xx ∈ A.optimalRowStrategies ∧ yy ∈ A.optimalColumnStrategies) ↔ A.IsSaddlePoint xx yy
```

## Dependencies

- optimalRowStrategies
- optimalColumnStrategies
- IsSaddlePoint
- mem_optimalRowStrategies_iff_E_ge
- mem_optimalColumnStrategies_iff_E_le
- IsPositiveAffineOf.symm
- Indifferent.symm
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
- lamB.aux.bddAbove
- lam.aux.bddAbove
- value_eq_minimax
- muB.aux.bddBelow
- mu.aux.bddBelow
- wsum_wsum_comm
