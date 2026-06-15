---
id: minimax-upper-bound
title: minimax_upper_bound
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreePlayerMinimaxFailure
  declarations:
    - minimax_upper_bound
uses:
---

# minimax_upper_bound

## Lean type

```lean
theorem minimax_upper_bound (x y : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (hy0 : 0 ≤ y) (hy1 : y ≤ 1) : G x y (1/2) ≤ (1 / 2 : ℝ)
```

## Dependencies

- none
