---
id: subgameAt-arena
title: subgameAt_arena
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - subgameAt_arena
uses:
  - subgameAt
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
  - Arena.Reachable.step
  - CPState.step
  - IsReachable.next
---

# subgameAt_arena

## Lean type

```lean
theorem subgameAt_arena (G : ExtensiveGame N U) (s : G.State) : (G.subgameAt s).toArena = G.toArena
```

## Dependencies

- subgameAt
- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
- Arena.Reachable.step
- CPState.step
- IsReachable.next
