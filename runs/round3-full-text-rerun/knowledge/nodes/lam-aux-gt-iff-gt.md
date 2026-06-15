---
id: lam-aux-gt-iff-gt
title: lam.aux_gt_iff_gt
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.MinimaxLoomis
  declarations:
    - lam.aux_gt_iff_gt
uses:
---

# lam.aux_gt_iff_gt

## Lean type

```lean
theorem lam.aux_gt_iff_gt (A : I → J → ℝ) (c : ℝ) (x : stdSimplex ℝ I) : c < lam.aux A x ↔ ∀ j, c < wsum x (fun i => A i j)
```

## Dependencies

- none
