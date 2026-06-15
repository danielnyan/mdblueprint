---
id: liftReachableSubgame
title: liftReachableSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - liftReachableSubgame
uses:
  - BehaviorProfile
  - reachableSubgameAt
---

# liftReachableSubgame

## Lean type

```lean
def liftReachableSubgame {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] {root : G.State} [(s : G.State) -> Decidable (Arena.Reachable G.toArena root s)] (base : G.BehaviorProfile) (beta : (G.reachableSubgameAt root).BehaviorProfile) : G.BehaviorProfile
```

## Dependencies

- BehaviorProfile
- reachableSubgameAt
