---
id: minimax-eq-one-half
title: minimax_eq_one_half
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.StrategicGame.ThreePlayerMinimaxFailure
  declarations:
    - minimax_eq_one_half
uses:
  - minimax_upper_bound
  - minimax_lower_bound
---

# minimax_eq_one_half

## Lean type

```lean
theorem minimax_eq_one_half : -- Witness z = 1/2 caps every (x,y) at 1/2. (∀ x y, 0 ≤ x → x ≤ 1 → 0 ≤ y → y ≤ 1 → G x y (1/2) ≤ (1 / 2 : ℝ)) ∧ -- Lower bound: every z ∈ [0,1] has max_{x,y} G(x,y,z) ≥ 1/2. (∀ z, 0 ≤ z → z ≤ 1 → (1 / 2 : ℝ) ≤ max (G 1 1 z) (G 0 0 z))
```

## Dependencies

- minimax_upper_bound
- minimax_lower_bound
