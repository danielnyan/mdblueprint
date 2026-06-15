---
id: support-complementarity-row
title: support_complementarity_row
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - support_complementarity_row
uses:
  - optimalRowStrategies
  - optimalColumnStrategies
  - mem_optimalRowStrategies_iff_E_ge
  - mem_optimalColumnStrategies_iff_E_le
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
---

# support_complementarity_row

## Lean type

```lean
theorem support_complementarity_row [DecidableEq I] (xx : stdSimplex ℝ I) (yy : stdSimplex ℝ J) (hxx : xx ∈ A.optimalRowStrategies) (hyy : yy ∈ A.optimalColumnStrategies) {i : I} (hi : 0 < xx.val i) : A.Ei i yy = A.value
```

## Dependencies

- optimalRowStrategies
- optimalColumnStrategies
- mem_optimalRowStrategies_iff_E_ge
- mem_optimalColumnStrategies_iff_E_le
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
