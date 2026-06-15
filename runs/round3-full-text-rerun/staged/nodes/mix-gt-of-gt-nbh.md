---
id: mix-gt-of-gt-nbh
title: mix_gt_of_gt_nbh
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - mix_gt_of_gt_nbh
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# mix_gt_of_gt_nbh

## Lean type

```lean
theorem mix_gt_of_gt_nbh (x y c : 𝕜) (H : c < x) : ∃ t : 𝕜, 0 < t ∧ t < 1 ∧ c < t * x + (1 - t) * y
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
