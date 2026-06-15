---
id: linear-comb-lt-of-le-lt
title: linear_comb_lt_of_le_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - linear_comb_lt_of_le_lt
uses:
---

# linear_comb_lt_of_le_lt

## Lean type

```lean
theorem linear_comb_lt_of_le_lt (x y c : 𝕜) (H1 : x ≤ c) (H2 : y < c) {α : 𝕜} (hα₀ : 0 ≤ α) (hα₁ : α < 1) : α * x + (1 - α) * y < c
```

## Dependencies

- none
