---
id: restrictReachableSubgame-deviate-liftReachableSubgame
title: restrictReachableSubgame_deviate_liftReachableSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - restrictReachableSubgame_deviate_liftReachableSubgame
uses:
  - BehaviorProfile
  - reachableSubgameAt
  - BehaviorStrategy
  - liftReachableSubgame
  - restrictReachableSubgame
---

# restrictReachableSubgame_deviate_liftReachableSubgame

## Lean type

```lean
theorem restrictReachableSubgame_deviate_liftReachableSubgame {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] [DecidableEq iota] {root : G.State} [(s : G.State) -> Decidable (Arena.Reachable G.toArena root s)] (beta : G.BehaviorProfile) (who : iota) (beta' : (G.reachableSubgameAt root).BehaviorStrategy who) : (beta.deviate who ((beta who).liftReachableSubgame beta')).restrictReachableSubgame root = (beta.restrictReachableSubgame root).deviate who beta'
```

## Dependencies

- BehaviorProfile
- reachableSubgameAt
- BehaviorStrategy
- liftReachableSubgame
- restrictReachableSubgame
