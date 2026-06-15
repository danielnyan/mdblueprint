---
id: reachableSubgameAt
title: reachableSubgameAt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - reachableSubgameAt
uses:
  - IsReachable.next
  - Arena.Reachable.step
  - CPState.step
  - ReachedSubgamePayoffTransfer.init
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
---

# reachableSubgameAt

## Lean type

```lean
def reachableSubgameAt (G : ExtensiveGame iota U) (root : G.State) : ExtensiveGame iota U
```

## Dependencies

- IsReachable.next
- Arena.Reachable.step
- CPState.step
- ReachedSubgamePayoffTransfer.init
- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
