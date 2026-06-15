---
id: minimax-lower-bound
title: minimax_lower_bound
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreePlayerMinimaxFailure
  declarations:
    - minimax_lower_bound
uses:
  - max_over_xy
---

# minimax_lower_bound

## Lean type

```lean
theorem minimax_lower_bound (z : ℝ) (hz0 : 0 ≤ z) (hz1 : z ≤ 1) : (1 / 2 : ℝ) ≤ max (G 1 1 z) (G 0 0 z)
```

## Dependencies

- max_over_xy
