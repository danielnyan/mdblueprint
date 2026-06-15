---
id: reachableSubgameAt-mover
title: reachableSubgameAt_mover
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - reachableSubgameAt_mover
uses:
  - reachableSubgameAt
---

# reachableSubgameAt_mover

## Lean type

```lean
@[simp] theorem reachableSubgameAt_mover (G : ExtensiveGame iota U) (root : G.State) (s : (G.reachableSubgameAt root).State) : (G.reachableSubgameAt root).mover s = G.mover s.1
```

## Dependencies

- reachableSubgameAt
