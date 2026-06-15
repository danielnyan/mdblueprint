---
id: diagonalGameValue-pos
title: diagonalGameValue_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.DiagonalGame
  declarations:
    - diagonalGameValue_pos
uses:
  - diagonalGame_value
---

# diagonalGameValue_pos

## Lean type

```lean
theorem diagonalGameValue_pos (a : I → ℝ) (hpos : ∀ i, 0 < a i) : 0 < diagonalGameValue a
```

## Dependencies

- diagonalGame_value
