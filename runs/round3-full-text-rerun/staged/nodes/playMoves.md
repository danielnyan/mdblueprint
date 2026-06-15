---
id: playMoves
title: playMoves
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.TicTacToe
  declarations:
    - playMoves
uses:
  - Pos
  - TTTState.move
  - TTTState.initial
---

# playMoves

## Lean type

```lean
def playMoves (moves : List Pos) : TTTState
```

## Dependencies

- Pos
- TTTState.move
- TTTState.initial
