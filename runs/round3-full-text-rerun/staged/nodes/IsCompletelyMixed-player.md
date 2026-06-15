---
id: IsCompletelyMixed-player
title: IsCompletelyMixed.player
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsCompletelyMixed.player
uses:
  - BehaviorProfile
  - IsCompletelyMixed
  - BehaviorStrategy
---

# IsCompletelyMixed.player

## Lean type

```lean
theorem IsCompletelyMixed.player {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] {beta : G.BehaviorProfile} (hbeta : IsCompletelyMixed beta) (i : iota) : BehaviorStrategy.IsCompletelyMixed (G
```

## Dependencies

- BehaviorProfile
- IsCompletelyMixed
- BehaviorStrategy
