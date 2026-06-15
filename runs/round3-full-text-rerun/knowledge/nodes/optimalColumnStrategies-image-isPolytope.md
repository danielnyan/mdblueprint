---
id: optimalColumnStrategies-image-isPolytope
title: optimalColumnStrategies_image_isPolytope
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.OptimalStrategySetPolytope
  declarations:
    - optimalColumnStrategies_image_isPolytope
uses:
  - optimalColumnStrategies
  - image_optimalColumnStrategies_eq
  - optimalColumnSet_convex
  - optimalColumnSet_isClosed
  - optimalColumnSet_isCompact
  - optimalColumnSet_nonempty
---

# optimalColumnStrategies_image_isPolytope

## Lean type

```lean
theorem optimalColumnStrategies_image_isPolytope : Convex ℝ (Subtype.val '' A.optimalColumnStrategies) ∧ IsClosed (Subtype.val '' A.optimalColumnStrategies) ∧ IsCompact (Subtype.val '' A.optimalColumnStrategies) ∧ (Subtype.val '' A.optimalColumnStrategies).Nonempty
```

## Dependencies

- optimalColumnStrategies
- image_optimalColumnStrategies_eq
- optimalColumnSet_convex
- optimalColumnSet_isClosed
- optimalColumnSet_isCompact
- optimalColumnSet_nonempty
