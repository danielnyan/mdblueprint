---
id: linear-comb-gt-of-ge-gt
title: linear_comb_gt_of_ge_gt
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - linear_comb_gt_of_ge_gt
uses:
---

# linear_comb_gt_of_ge_gt

## Lean type

```lean
theorem linear_comb_gt_of_ge_gt (x y c : 𝕜) (H1 : c ≤ x) (H2 : c < y) {α : 𝕜} (hα₀ : 0 ≤ α) (hα₁ : α < 1) : c < α * x + (1 - α) * y
```

## Dependencies

- none
