---
id: actionProb
title: actionProb
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - actionProb
uses:
  - BehaviorProfile
---

# actionProb

## Lean type

```lean
def actionProb {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] (beta : G.BehaviorProfile) (s : G.State) (a : G.Action s) : Real
```

## Dependencies

- BehaviorProfile
