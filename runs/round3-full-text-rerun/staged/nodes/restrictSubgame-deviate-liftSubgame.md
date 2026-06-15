---
id: restrictSubgame-deviate-liftSubgame
title: restrictSubgame_deviate_liftSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - restrictSubgame_deviate_liftSubgame
uses:
  - BehaviorProfile
  - subgameAt
  - BehaviorStrategy
  - liftSubgame
  - restrictSubgame
  - restrictSubgame_deviate
  - restrictSubgame_liftSubgame
  - actionProb
  - IsReachable.next
  - ReachedSubgamePayoffTransfer.init
---

# restrictSubgame_deviate_liftSubgame

## Lean type

```lean
theorem restrictSubgame_deviate_liftSubgame {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] [DecidableEq iota] (beta : G.BehaviorProfile) (who : iota) {root : G.State} (beta' : (G.subgameAt root).BehaviorStrategy who) : (beta.deviate who beta'.liftSubgame).restrictSubgame root = (beta.restrictSubgame root).deviate who beta'
```

## Dependencies

- BehaviorProfile
- subgameAt
- BehaviorStrategy
- liftSubgame
- restrictSubgame
- restrictSubgame_deviate
- restrictSubgame_liftSubgame
- actionProb
- IsReachable.next
- ReachedSubgamePayoffTransfer.init
