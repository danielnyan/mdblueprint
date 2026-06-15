---
id: place
title: place
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.TicTacToe
  declarations:
    - place
uses:
  - Board
  - Pos
---

# place

## Lean type

```lean
def place (b : Board) (p : Pos) (m : Mark) : Board
```

## Dependencies

- Board
- Pos
