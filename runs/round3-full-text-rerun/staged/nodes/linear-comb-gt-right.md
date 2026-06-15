---
id: linear-comb-gt-right
title: linear_comb_gt_right
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - linear_comb_gt_right
uses:
---

# linear_comb_gt_right

## Lean type

```lean
theorem linear_comb_gt_right {x y : 𝕜} (H : y < x) {α : 𝕜} (Hα : 0 < α) : y < α * x + (1 - α) * y
```

## Dependencies

- none
