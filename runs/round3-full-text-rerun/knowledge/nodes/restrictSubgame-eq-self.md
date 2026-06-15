---
id: restrictSubgame-eq-self
title: restrictSubgame_eq_self
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - restrictSubgame_eq_self
uses:
  - BehaviorProfile
  - restrictSubgame
---

# restrictSubgame_eq_self

## Lean type

```lean
theorem restrictSubgame_eq_self {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] (beta : G.BehaviorProfile) (root : G.State) : beta.restrictSubgame root = beta
```

## Dependencies

- BehaviorProfile
- restrictSubgame
