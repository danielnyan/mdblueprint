---
id: max-over-xy
title: max_over_xy
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreePlayerMinimaxFailure
  declarations:
    - max_over_xy
uses:
---

# max_over_xy

## Lean type

```lean
theorem max_over_xy (z : ℝ) (hz0 : 0 ≤ z) (hz1 : z ≤ 1) : max z (1 - z) ≤ max (G 1 1 z) (G 0 0 z)
```

## Dependencies

- none
