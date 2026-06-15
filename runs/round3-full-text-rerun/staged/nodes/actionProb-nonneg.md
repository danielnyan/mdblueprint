---
id: actionProb-nonneg
title: actionProb_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - actionProb_nonneg
uses:
  - BehaviorProfile
  - actionProb
---

# actionProb_nonneg

## Lean type

```lean
theorem actionProb_nonneg {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] (beta : G.BehaviorProfile) (s : G.State) (a : G.Action s) : 0 <= beta.actionProb s a
```

## Dependencies

- BehaviorProfile
- actionProb
