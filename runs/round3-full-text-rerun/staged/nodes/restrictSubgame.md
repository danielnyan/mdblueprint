---
id: restrictSubgame
title: restrictSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - restrictSubgame
uses:
  - BehaviorProfile
  - subgameAt
---

# restrictSubgame

## Lean type

```lean
def restrictSubgame {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] (beta : G.BehaviorProfile) (root : G.State) : (G.subgameAt root).BehaviorProfile
```

## Dependencies

- BehaviorProfile
- subgameAt
