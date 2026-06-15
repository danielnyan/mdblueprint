---
id: lamB-aux-gt-iff-gt
title: lamB.aux_gt_iff_gt
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Minimax.Loomis
  declarations:
    - lamB.aux_gt_iff_gt
uses:
---

# lamB.aux_gt_iff_gt

## Lean type

```lean
theorem lamB.aux_gt_iff_gt (A B : I → J → ℝ) (c : ℝ) (x : stdSimplex ℝ I) : c < lamB.aux A B x ↔ ∀ j, c < colRatio A B x j
```

## Dependencies

- none
