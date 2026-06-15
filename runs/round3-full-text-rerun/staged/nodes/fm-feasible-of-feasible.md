---
id: fm-feasible-of-feasible
title: fm_feasible_of_feasible
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - fm_feasible_of_feasible
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - fmA
  - fmB
  - rowEval
  - PosRows
  - NegRows
---

# fm_feasible_of_feasible

## Lean type

```lean
theorem fm_feasible_of_feasible (A : I → Fin (n+1) → 𝕜) (b : I → 𝕜) (hfeas : IsFeasible A b) : IsFeasible (fmA A) (fmB A b)
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- fmA
- fmB
- rowEval
- PosRows
- NegRows
