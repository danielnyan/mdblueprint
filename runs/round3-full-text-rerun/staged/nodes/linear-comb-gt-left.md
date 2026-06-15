---
id: linear-comb-gt-left
title: linear_comb_gt_left
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - linear_comb_gt_left
uses:
---

# linear_comb_gt_left

## Lean type

```lean
theorem linear_comb_gt_left {x y : 𝕜} (H : x < y) {α : 𝕜} (Hα : α < 1) : x < α * x + (1 - α) * y
```

## Dependencies

- none
