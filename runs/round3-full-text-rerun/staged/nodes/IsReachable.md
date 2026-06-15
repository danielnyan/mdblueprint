---
id: IsReachable
title: IsReachable
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Subgame
  declarations:
    - IsReachable
uses:
  - ReachedSubgamePayoffTransfer.init
---

# IsReachable

## Lean type

```lean
def IsReachable (G : ExtensiveGame N U) (s : G.State) : Prop
```

## Dependencies

- ReachedSubgamePayoffTransfer.init
