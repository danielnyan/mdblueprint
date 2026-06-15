---
id: wsum-continuous
title: wsum_continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - wsum_continuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - stdSimplex.continuous_coord
---

# wsum_continuous

## Lean type

```lean
theorem wsum_continuous (f : I → ℝ) : Continuous fun x : stdSimplex ℝ I => wsum x f
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- stdSimplex.continuous_coord
