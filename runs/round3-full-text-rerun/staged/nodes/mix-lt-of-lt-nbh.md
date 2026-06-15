---
id: mix-lt-of-lt-nbh
title: mix_lt_of_lt_nbh
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - mix_lt_of_lt_nbh
uses:
  - mix_gt_of_gt_nbh
---

# mix_lt_of_lt_nbh

## Lean type

```lean
theorem mix_lt_of_lt_nbh (x y c : 𝕜) (H : x < c) : ∃ t : 𝕜, 0 < t ∧ t < 1 ∧ t * x + (1 - t) * y < c
```

## Dependencies

- mix_gt_of_gt_nbh
