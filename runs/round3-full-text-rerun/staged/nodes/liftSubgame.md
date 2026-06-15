---
id: liftSubgame
title: liftSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - liftSubgame
uses:
  - subgameAt
  - BehaviorProfile
---

# liftSubgame

## Lean type

```lean
def liftSubgame {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] {root : G.State} (beta : (G.subgameAt root).BehaviorProfile) : G.BehaviorProfile
```

## Dependencies

- subgameAt
- BehaviorProfile
