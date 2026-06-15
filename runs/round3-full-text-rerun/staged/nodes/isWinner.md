---
id: isWinner
title: isWinner
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.TicTacToe
  declarations:
    - isWinner
uses:
  - Board
  - winLines
---

# isWinner

## Lean type

```lean
def isWinner (b : Board) (m : Mark) : Bool
```

## Dependencies

- Board
- winLines
