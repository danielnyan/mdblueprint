---
id: centipedePrefixArena
title: centipedePrefixArena
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CentipedeGame
  declarations:
    - centipedePrefixArena
uses:
  - IsReachable.next
  - ReachedSubgamePayoffTransfer.init
---

# centipedePrefixArena

## Lean type

```lean
def centipedePrefixArena : ExtensiveGame (Fin 2) ℤ
```

## Dependencies

- IsReachable.next
- ReachedSubgamePayoffTransfer.init
