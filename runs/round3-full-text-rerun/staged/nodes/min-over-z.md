---
id: min-over-z
title: min_over_z
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreePlayerMinimaxFailure
  declarations:
    - min_over_z
uses:
---

# min_over_z

## Lean type

```lean
theorem min_over_z (x y : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (hy0 : 0 ≤ y) (hy1 : y ≤ 1) : ∀ z, 0 ≤ z → z ≤ 1 → min (x * y) ((1 - x) * (1 - y)) ≤ G x y z
```

## Dependencies

- none
