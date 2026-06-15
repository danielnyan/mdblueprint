---
id: restrictReachableSubgame
title: restrictReachableSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - restrictReachableSubgame
uses:
  - BehaviorProfile
  - reachableSubgameAt
---

# restrictReachableSubgame

## Lean type

```lean
def restrictReachableSubgame {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] (beta : G.BehaviorProfile) (root : G.State) : (G.reachableSubgameAt root).BehaviorProfile
```

## Dependencies

- BehaviorProfile
- reachableSubgameAt
