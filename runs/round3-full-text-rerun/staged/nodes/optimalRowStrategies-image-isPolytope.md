---
id: optimalRowStrategies-image-isPolytope
title: optimalRowStrategies_image_isPolytope
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.OptimalStrategySetPolytope
  declarations:
    - optimalRowStrategies_image_isPolytope
uses:
  - optimalRowStrategies
  - image_optimalRowStrategies_eq
  - optimalRowSet_convex
  - optimalRowSet_isClosed
  - optimalRowSet_isCompact
  - optimalRowSet_nonempty
---

# optimalRowStrategies_image_isPolytope

## Lean type

```lean
theorem optimalRowStrategies_image_isPolytope : Convex ℝ (Subtype.val '' A.optimalRowStrategies) ∧ IsClosed (Subtype.val '' A.optimalRowStrategies) ∧ IsCompact (Subtype.val '' A.optimalRowStrategies) ∧ (Subtype.val '' A.optimalRowStrategies).Nonempty
```

## Dependencies

- optimalRowStrategies
- image_optimalRowStrategies_eq
- optimalRowSet_convex
- optimalRowSet_isClosed
- optimalRowSet_isCompact
- optimalRowSet_nonempty
