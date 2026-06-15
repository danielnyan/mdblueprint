---
id: IsCompletelyMixedWithPositiveReach-mixed
title: IsCompletelyMixedWithPositiveReach.mixed
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsCompletelyMixedWithPositiveReach.mixed
uses:
  - BehaviorProfile
  - IsCompletelyMixedWithPositiveReach
  - IsCompletelyMixed
---

# IsCompletelyMixedWithPositiveReach.mixed

## Lean type

```lean
theorem IsCompletelyMixedWithPositiveReach.mixed {G : ExtensiveGame iota U} [DecidableEq G.State] [(s : G.State) -> Fintype (G.Action s)] {beta : G.BehaviorProfile} {fuel : Nat} (hbeta : IsCompletelyMixedWithPositiveReach beta fuel) : IsCompletelyMixed beta
```

## Dependencies

- BehaviorProfile
- IsCompletelyMixedWithPositiveReach
- IsCompletelyMixed
