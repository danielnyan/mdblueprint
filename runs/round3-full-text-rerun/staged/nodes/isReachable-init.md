---
id: isReachable-init
title: isReachable_init
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - isReachable_init
uses:
  - IsReachable
  - ReachedSubgamePayoffTransfer.init
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
---

# isReachable_init

## Lean type

```lean
theorem isReachable_init (G : ExtensiveGame N U) : G.IsReachable G.init
```

## Dependencies

- IsReachable
- ReachedSubgamePayoffTransfer.init
- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
