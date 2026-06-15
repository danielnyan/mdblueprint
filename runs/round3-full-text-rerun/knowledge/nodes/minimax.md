---
id: minimax
title: minimax
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Minimax
  declarations:
    - minimax
uses:
  - minimax_pos
---

# minimax

## Lean type

```lean
theorem minimax (A : I → J → 𝕜) : ∃ (x : I → 𝕜) (y : J → 𝕜) (v : 𝕜), (∀ i, 0 ≤ x i) ∧ (∑ i, x i = 1) ∧ (∀ j, 0 ≤ y j) ∧ (∑ j, y j = 1) ∧ (∀ j, v ≤ ∑ i, x i * A i j) ∧ (∀ i, ∑ j, A i j * y j ≤ v)
```

## Dependencies

- minimax_pos
