---
id: minimax-optimal-strategies
title: minimax_optimal_strategies
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGame
  declarations:
    - minimax_optimal_strategies
uses:
  - exists_xx_lam0
  - exists_yy_mu0
  - minmax_from_general
---

# minimax_optimal_strategies

## Lean type

```lean
theorem minimax_optimal_strategies : ∃ (xx : stdSimplex ℝ I) (yy : stdSimplex ℝ J) (v : ℝ), (∀ j : J, A.Ej xx j ≥ v) ∧ (∀ i : I, A.Ei i yy ≤ v)
```

## Dependencies

- exists_xx_lam0
- exists_yy_mu0
- minmax_from_general
