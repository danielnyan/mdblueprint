---
id: image-optimalRowStrategies-eq
title: image_optimalRowStrategies_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.OptimalStrategySetPolytope
  declarations:
    - image_optimalRowStrategies_eq
uses:
  - optimalRowStrategies
  - optimalRowSet
  - Profile.ext
  - mem_optimalRowStrategies_iff_E_ge
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
  - wsum_wsum_comm
  - ge_iff_simplex_ge
---

# image_optimalRowStrategies_eq

## Lean type

```lean
theorem image_optimalRowStrategies_eq : (Subtype.val '' A.optimalRowStrategies) = A.optimalRowSet
```

## Dependencies

- optimalRowStrategies
- optimalRowSet
- Profile.ext
- mem_optimalRowStrategies_iff_E_ge
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
- wsum_wsum_comm
- ge_iff_simplex_ge
