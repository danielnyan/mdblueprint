---
id: TTTState-isOver
title: TTTState.isOver
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.TicTacToe
  declarations:
    - TTTState.isOver
uses:
  - isWinner
  - Board
  - emptyPositions
  - isEmpty
---

# TTTState.isOver

## Lean type

```lean
def TTTState.isOver (s : TTTState) : Bool
```

## Dependencies

- isWinner
- Board
- emptyPositions
- isEmpty
