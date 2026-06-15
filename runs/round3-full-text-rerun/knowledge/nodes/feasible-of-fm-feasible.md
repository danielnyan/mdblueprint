---
id: feasible-of-fm-feasible
title: feasible_of_fm_feasible
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - feasible_of_fm_feasible
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - fmA
  - fmB
  - PosRows
  - NegRows
  - rowEval
  - ZeroRows
---

# feasible_of_fm_feasible

## Lean type

```lean
theorem feasible_of_fm_feasible (A : I → Fin (n+1) → 𝕜) (b : I → 𝕜) (hred : IsFeasible (fmA A) (fmB A b)) : IsFeasible A b
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- fmA
- fmB
- PosRows
- NegRows
- rowEval
- ZeroRows
