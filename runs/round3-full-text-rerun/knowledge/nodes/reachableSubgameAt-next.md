---
id: reachableSubgameAt-next
title: reachableSubgameAt_next
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - reachableSubgameAt_next
uses:
  - reachableSubgameAt
  - IsReachable.next
  - Arena.Reachable.step
  - CPState.step
---

# reachableSubgameAt_next

## Lean type

```lean
@[simp] theorem reachableSubgameAt_next (G : ExtensiveGame iota U) (root : G.State) (s : (G.reachableSubgameAt root).State) (a : (G.reachableSubgameAt root).Action s) : (G.reachableSubgameAt root).next s a = ⟨G.next s.1 a, s.2.step' a⟩
```

## Dependencies

- reachableSubgameAt
- IsReachable.next
- Arena.Reachable.step
- CPState.step
