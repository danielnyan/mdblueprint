---
id: TTTState-move
title: TTTState.move
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.TicTacToe
  declarations:
    - TTTState.move
uses:
  - Pos
  - Board
  - Mark.other
---

# TTTState.move

## Lean type

```lean
def TTTState.move (s : TTTState) (p : Pos) : TTTState
```

## Dependencies

- Pos
- Board
- Mark.other
