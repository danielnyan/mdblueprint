---
id: reachableSubgameAt-init
title: reachableSubgameAt_init
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - reachableSubgameAt_init
uses:
  - reachableSubgameAt
  - ReachedSubgamePayoffTransfer.init
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
---

# reachableSubgameAt_init

## Lean type

```lean
@[simp] theorem reachableSubgameAt_init (G : ExtensiveGame iota U) (root : G.State) : (G.reachableSubgameAt root).init = ⟨root, Arena.Reachable.refl _⟩
```

## Dependencies

- reachableSubgameAt
- ReachedSubgamePayoffTransfer.init
- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
