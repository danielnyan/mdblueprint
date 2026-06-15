---
id: diagonalGame-row-guarantee
title: diagonalGame_row_guarantee
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.DiagonalGame
  declarations:
    - diagonalGame_row_guarantee
uses:
  - diagonalGame_value
  - diagonalGame
---

# diagonalGame_row_guarantee

## Lean type

```lean
theorem diagonalGame_row_guarantee (a : I → ℝ) (hpos : ∀ i, 0 < a i) : ∀ j, diagonalGameValue a ≤ (diagonalGame a).Ej (diagonalGameStrategy a hpos) j
```

## Dependencies

- diagonalGame_value
- diagonalGame
