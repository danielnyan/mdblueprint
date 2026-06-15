---
id: emptyPositions
title: emptyPositions
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.TicTacToe
  declarations:
    - emptyPositions
uses:
  - Board
  - Pos
  - allPos
  - isEmpty
---

# emptyPositions

## Lean type

```lean
def emptyPositions (b : Board) : List Pos
```

## Dependencies

- Board
- Pos
- allPos
- isEmpty
