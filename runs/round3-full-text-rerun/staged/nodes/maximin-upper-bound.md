---
id: maximin-upper-bound
title: maximin_upper_bound
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreePlayerMinimaxFailure
  declarations:
    - maximin_upper_bound
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# maximin_upper_bound

## Lean type

```lean
theorem maximin_upper_bound (x y : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (hy0 : 0 ≤ y) (hy1 : y ≤ 1) : min (x * y) ((1 - x) * (1 - y)) ≤ (1 / 4 : ℝ)
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
