---
id: IsReachable-next
title: IsReachable.next
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - IsReachable.next
uses:
  - IsReachable
  - Arena.Reachable.step
  - CPState.step
---

# IsReachable.next

## Lean type

```lean
theorem IsReachable.next {G : ExtensiveGame N U} {s : G.State} (h : G.IsReachable s) (a : G.Action s) : G.IsReachable (G.next s a)
```

## Dependencies

- IsReachable
- Arena.Reachable.step
- CPState.step
