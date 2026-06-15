---
id: support-complementarity-column
title: support_complementarity_column
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - support_complementarity_column
uses:
  - optimalRowStrategies
  - optimalColumnStrategies
  - mem_optimalRowStrategies_iff_E_ge
  - mem_optimalColumnStrategies_iff_E_le
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
  - wsum_wsum_comm
---

# support_complementarity_column

## Lean type

```lean
theorem support_complementarity_column [DecidableEq J] (xx : stdSimplex ℝ I) (yy : stdSimplex ℝ J) (hxx : xx ∈ A.optimalRowStrategies) (hyy : yy ∈ A.optimalColumnStrategies) {j : J} (hj : 0 < yy.val j) : A.Ej xx j = A.value
```

## Dependencies

- optimalRowStrategies
- optimalColumnStrategies
- mem_optimalRowStrategies_iff_E_ge
- mem_optimalColumnStrategies_iff_E_le
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
- wsum_wsum_comm
