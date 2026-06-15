---
id: IsBehaviorNashEq
title: IsBehaviorNashEq
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsBehaviorNashEq
uses:
  - isEmpty
  - BehaviorProfile
  - BehaviorStrategy
  - expectedPayoff
---

# IsBehaviorNashEq

## Lean type

```lean
def IsBehaviorNashEq (G : ExtensiveGame iota Real) [(s : G.State) -> Fintype (G.Action s)] [(s : G.State) -> Decidable (IsEmpty (G.Action s))] [DecidableEq iota] (beta : G.BehaviorProfile) (fuel : Nat) : Prop
```

## Dependencies

- isEmpty
- BehaviorProfile
- BehaviorStrategy
- expectedPayoff
