---
id: maximin-lower-bound
title: maximin_lower_bound
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreePlayerMinimaxFailure
  declarations:
    - maximin_lower_bound
uses:
  - min_over_z
  - min_at_half
---

# maximin_lower_bound

## Lean type

```lean
theorem maximin_lower_bound : ∀ z, 0 ≤ z → z ≤ 1 → (1 / 4 : ℝ) ≤ G (1/2) (1/2) z
```

## Dependencies

- min_over_z
- min_at_half
