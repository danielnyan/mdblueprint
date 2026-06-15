---
id: maximin-eq-one-quarter
title: maximin_eq_one_quarter
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreePlayerMinimaxFailure
  declarations:
    - maximin_eq_one_quarter
uses:
  - maximin_lower_bound
  - maximin_upper_bound
---

# maximin_eq_one_quarter

## Lean type

```lean
theorem maximin_eq_one_quarter : -- Witness x = y = 1/2 achieves at least 1/4 against every z. (∀ z, 0 ≤ z → z ≤ 1 → (1 / 4 : ℝ) ≤ G (1/2) (1/2) z) ∧ -- Upper bound: every (x,y) ∈ [0,1]² has min_z G(x,y,z) ≤ 1/4. (∀ x y, 0 ≤ x → x ≤ 1 → 0 ≤ y → y ≤ 1 → min (x * y) ((1 - x) * (1 - y)) ≤ (1 / 4 : ℝ))
```

## Dependencies

- maximin_lower_bound
- maximin_upper_bound
