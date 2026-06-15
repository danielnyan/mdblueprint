---
id: probAt
title: probAt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - probAt
uses:
  - BehaviorProfile
---

# probAt

## Lean type

```lean
def probAt {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] (beta : G.BehaviorProfile) {s : G.State} {i : iota} (h : G.mover s = some i) (a : G.Action s) : Real
```

## Dependencies

- BehaviorProfile
