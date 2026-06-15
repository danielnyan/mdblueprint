---
id: diagonalGame-value
title: diagonalGame_value
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.DiagonalGame
  declarations:
    - diagonalGame_value
uses:
  - diagonalGame
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - common_guarantee_eq_value
  - diagonalGame_row_guarantee
  - diagonalGame_column_guarantee
---

# diagonalGame_value

## Lean type

```lean
theorem diagonalGame_value (a : I → ℝ) (hpos : ∀ i, 0 < a i) : (diagonalGame a).value = diagonalGameValue a
```

## Dependencies

- diagonalGame
- IsPositiveAffineOf.symm
- Indifferent.symm
- common_guarantee_eq_value
- diagonalGame_row_guarantee
- diagonalGame_column_guarantee
