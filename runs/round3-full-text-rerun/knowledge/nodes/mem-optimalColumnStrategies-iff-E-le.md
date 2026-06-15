---
id: mem-optimalColumnStrategies-iff-E-le
title: mem_optimalColumnStrategies_iff_E_le
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - mem_optimalColumnStrategies_iff_E_le
uses:
  - optimalColumnStrategies
  - le_iff_simplex_le
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
  - value_eq_minimax
  - muB.aux.bddBelow
  - mu.aux.bddBelow
---

# mem_optimalColumnStrategies_iff_E_le

## Lean type

```lean
theorem mem_optimalColumnStrategies_iff_E_le (yy : stdSimplex ℝ J) : yy ∈ A.optimalColumnStrategies ↔ ∀ x' : stdSimplex ℝ I, A.E x' yy ≤ A.value
```

## Dependencies

- optimalColumnStrategies
- le_iff_simplex_le
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
- value_eq_minimax
- muB.aux.bddBelow
- mu.aux.bddBelow
