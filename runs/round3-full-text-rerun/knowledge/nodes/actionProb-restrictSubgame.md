---
id: actionProb-restrictSubgame
title: actionProb_restrictSubgame
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - actionProb_restrictSubgame
uses:
  - BehaviorProfile
  - restrictSubgame
  - actionProb
---

# actionProb_restrictSubgame

## Lean type

```lean
@[simp] theorem actionProb_restrictSubgame {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] (beta : G.BehaviorProfile) (root s : G.State) (a : G.Action s) : (beta.restrictSubgame root).actionProb s a = beta.actionProb s a
```

## Dependencies

- BehaviorProfile
- restrictSubgame
- actionProb
