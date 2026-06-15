---
id: image-optimalColumnStrategies-eq
title: image_optimalColumnStrategies_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.OptimalStrategySetPolytope
  declarations:
    - image_optimalColumnStrategies_eq
uses:
  - optimalColumnStrategies
  - optimalColumnSet
  - Profile.ext
  - mem_optimalColumnStrategies_iff_E_le
  - stdSimplex.pure
  - Lottery.pure
  - wsum_pure_apply
  - le_iff_simplex_le
---

# image_optimalColumnStrategies_eq

## Lean type

```lean
theorem image_optimalColumnStrategies_eq : (Subtype.val '' A.optimalColumnStrategies) = A.optimalColumnSet
```

## Dependencies

- optimalColumnStrategies
- optimalColumnSet
- Profile.ext
- mem_optimalColumnStrategies_iff_E_le
- stdSimplex.pure
- Lottery.pure
- wsum_pure_apply
- le_iff_simplex_le
