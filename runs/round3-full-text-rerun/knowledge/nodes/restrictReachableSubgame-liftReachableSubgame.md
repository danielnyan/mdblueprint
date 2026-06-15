---
id: restrictReachableSubgame-liftReachableSubgame
title: restrictReachableSubgame_liftReachableSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - restrictReachableSubgame_liftReachableSubgame
uses:
  - BehaviorProfile
  - reachableSubgameAt
  - liftReachableSubgame
  - restrictReachableSubgame
---

# restrictReachableSubgame_liftReachableSubgame

## Lean type

```lean
@[simp] theorem restrictReachableSubgame_liftReachableSubgame {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] {root : G.State} [(s : G.State) -> Decidable (Arena.Reachable G.toArena root s)] (base : G.BehaviorProfile) (beta : (G.reachableSubgameAt root).BehaviorProfile) : (base.liftReachableSubgame beta).restrictReachableSubgame root = beta
```

## Dependencies

- BehaviorProfile
- reachableSubgameAt
- liftReachableSubgame
- restrictReachableSubgame
