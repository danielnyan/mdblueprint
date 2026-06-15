---
id: restrictSubgame-deviate
title: restrictSubgame_deviate
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - restrictSubgame_deviate
uses:
  - BehaviorProfile
  - BehaviorStrategy
  - restrictSubgame
---

# restrictSubgame_deviate

## Lean type

```lean
theorem restrictSubgame_deviate {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] [DecidableEq iota] (beta : G.BehaviorProfile) (who : iota) (beta' : G.BehaviorStrategy who) (root : G.State) : (beta.deviate who beta').restrictSubgame root = (beta.restrictSubgame root).deviate who (beta'.restrictSubgame root)
```

## Dependencies

- BehaviorProfile
- BehaviorStrategy
- restrictSubgame
