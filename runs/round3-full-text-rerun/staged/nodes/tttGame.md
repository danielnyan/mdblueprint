---
id: tttGame
title: tttGame
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.TicTacToe
  declarations:
    - tttGame
uses:
  - Pos
  - IsReachable.next
  - TTTState.isOver
  - CPState.isOver
  - TTTState.move
  - ReachedSubgamePayoffTransfer.init
  - TTTState.initial
  - isWinner
  - Board
---

# tttGame

## Lean type

```lean
def tttGame : ExtensiveGame (Fin 2) ℤ
```

## Dependencies

- Pos
- IsReachable.next
- TTTState.isOver
- CPState.isOver
- TTTState.move
- ReachedSubgamePayoffTransfer.init
- TTTState.initial
- isWinner
- Board
