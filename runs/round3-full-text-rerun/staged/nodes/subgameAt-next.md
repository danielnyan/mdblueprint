---
id: subgameAt-next
title: subgameAt_next
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BehaviorStrategy
  declarations:
    - subgameAt_next
uses:
  - subgameAt
  - IsReachable.next
  - isEmpty
  - reachableSubgameAt
---

# subgameAt_next

## Lean type

```lean
@[simp] theorem subgameAt_next (G : ExtensiveGame iota U) (s t : G.State) (a : G.Action t) : (G.subgameAt s).next t a = G.next t a
```

## Dependencies

- subgameAt
- IsReachable.next
- isEmpty
- reachableSubgameAt
