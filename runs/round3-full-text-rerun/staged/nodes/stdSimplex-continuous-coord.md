---
id: stdSimplex-continuous-coord
title: stdSimplex.continuous_coord
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.Simplex
  declarations:
    - stdSimplex.continuous_coord
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
---

# stdSimplex.continuous_coord

## Lean type

```lean
theorem stdSimplex.continuous_coord (i : I) : Continuous fun x : stdSimplex ℝ I => x.val i
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
