---
id: subgameAt-mover
title: subgameAt_mover
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - subgameAt_mover
uses:
  - subgameAt
---

# subgameAt_mover

## Lean type

```lean
@[simp] theorem subgameAt_mover (G : ExtensiveGame iota U) (s t : G.State) : (G.subgameAt s).mover t = G.mover t
```

## Dependencies

- subgameAt
