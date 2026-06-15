---
id: tPush-mem-Icc
title: tPush_mem_Icc
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - tPush_mem_Icc
uses:
  - BigSimplex
  - deficit_nonneg
---

# tPush_mem_Icc

## Lean type

```lean
lemma tPush_mem_Icc (x : BigSimplex card) : tPush card x ∈ Set.Icc (0 : ℝ) 1
```

## Dependencies

- BigSimplex
- deficit_nonneg
