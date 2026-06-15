---
id: centipede
title: centipede
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CentipedeGame
  declarations:
    - centipede
uses:
  - IsReachable.next
  - Arena.Reachable.step
  - CPState.step
  - ReachedSubgamePayoffTransfer.init
  - TTTState.isOver
  - CPState.isOver
---

# centipede

## Lean type

```lean
def centipede (n : ℕ) : ExtensiveGame (Fin 2) ℤ
```

## Dependencies

- IsReachable.next
- Arena.Reachable.step
- CPState.step
- ReachedSubgamePayoffTransfer.init
- TTTState.isOver
- CPState.isOver
