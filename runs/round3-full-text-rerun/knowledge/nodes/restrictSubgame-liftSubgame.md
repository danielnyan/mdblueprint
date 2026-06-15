---
id: restrictSubgame-liftSubgame
title: restrictSubgame_liftSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - restrictSubgame_liftSubgame
uses:
  - subgameAt
  - BehaviorProfile
  - restrictSubgame
---

# restrictSubgame_liftSubgame

## Lean type

```lean
@[simp] theorem restrictSubgame_liftSubgame {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] {root : G.State} (beta : (G.subgameAt root).BehaviorProfile) : beta.liftSubgame.restrictSubgame root = beta
```

## Dependencies

- subgameAt
- BehaviorProfile
- restrictSubgame
