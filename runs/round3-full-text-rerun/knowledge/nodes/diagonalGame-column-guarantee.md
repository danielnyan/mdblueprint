---
id: diagonalGame-column-guarantee
title: diagonalGame_column_guarantee
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.DiagonalGame
  declarations:
    - diagonalGame_column_guarantee
uses:
  - diagonalGame
  - diagonalGame_value
---

# diagonalGame_column_guarantee

## Lean type

```lean
theorem diagonalGame_column_guarantee (a : I → ℝ) (hpos : ∀ i, 0 < a i) : ∀ i, (diagonalGame a).Ei i (diagonalGameStrategy a hpos) ≤ diagonalGameValue a
```

## Dependencies

- diagonalGame
- diagonalGame_value
