---
id: BehaviorStrategy
title: BehaviorStrategy
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - BehaviorStrategy
uses:
---

# BehaviorStrategy

## Lean type

```lean
def BehaviorStrategy (G : ExtensiveGame iota U) (i : iota) [(s : G.State) -> Fintype (G.Action s)] : Type _
```

## Dependencies

- none
