---
id: IsCompletelyMixed-actionProb-pos
title: IsCompletelyMixed.actionProb_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - IsCompletelyMixed.actionProb_pos
uses:
  - BehaviorProfile
  - IsCompletelyMixed
  - actionProb
---

# IsCompletelyMixed.actionProb_pos

## Lean type

```lean
theorem IsCompletelyMixed.actionProb_pos {G : ExtensiveGame iota U} [(s : G.State) -> Fintype (G.Action s)] {beta : G.BehaviorProfile} (hbeta : IsCompletelyMixed beta) {s : G.State} {i : iota} (hm : G.mover s = some i) (a : G.Action s) : 0 < beta.actionProb s a
```

## Dependencies

- BehaviorProfile
- IsCompletelyMixed
- actionProb
