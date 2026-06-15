---
id: BehaviorProfile
title: BehaviorProfile
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - BehaviorProfile
uses:
  - BehaviorStrategy
---

# BehaviorProfile

## Lean type

```lean
def BehaviorProfile (G : ExtensiveGame iota U) [(s : G.State) -> Fintype (G.Action s)] : Type _
```

## Dependencies

- BehaviorStrategy
