---
id: mem-optimalRowStrategies-iff-E-ge
title: mem_optimalRowStrategies_iff_E_ge
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - mem_optimalRowStrategies_iff_E_ge
uses:
  - optimalRowStrategies
  - wsum_wsum_comm
  - ge_iff_simplex_ge
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
  - lamB.aux.bddAbove
  - lam.aux.bddAbove
  - value_eq_maximin
---

# mem_optimalRowStrategies_iff_E_ge

## Lean type

```lean
theorem mem_optimalRowStrategies_iff_E_ge (xx : stdSimplex ℝ I) : xx ∈ A.optimalRowStrategies ↔ ∀ y' : stdSimplex ℝ J, A.value ≤ A.E xx y'
```

## Dependencies

- optimalRowStrategies
- wsum_wsum_comm
- ge_iff_simplex_ge
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
- lamB.aux.bddAbove
- lam.aux.bddAbove
- value_eq_maximin
