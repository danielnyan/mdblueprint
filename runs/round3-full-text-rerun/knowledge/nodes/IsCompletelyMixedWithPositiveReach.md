---
id: IsCompletelyMixedWithPositiveReach
title: IsCompletelyMixedWithPositiveReach
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsCompletelyMixedWithPositiveReach
uses:
  - BehaviorProfile
  - IsCompletelyMixed
---

# IsCompletelyMixedWithPositiveReach

## Lean type

```lean
def IsCompletelyMixedWithPositiveReach {G : ExtensiveGame iota U} [DecidableEq G.State] [(s : G.State) -> Fintype (G.Action s)] (beta : G.BehaviorProfile) (fuel : Nat) : Prop
```

## Dependencies

- BehaviorProfile
- IsCompletelyMixed
