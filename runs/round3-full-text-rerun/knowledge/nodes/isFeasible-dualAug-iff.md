---
id: isFeasible-dualAug-iff
title: isFeasible_dualAug_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearProgramming.StrongDuality
  declarations:
    - isFeasible_dualAug_iff
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - dualAugA
  - dualAugB
  - PrimalFeasible
  - rowEval
---

# isFeasible_dualAug_iff

## Lean type

```lean
theorem isFeasible_dualAug_iff (A : I → Fin n → 𝕜) (b : I → 𝕜) : IsFeasible (dualAugA A) (dualAugB b) ↔ PrimalFeasible A b
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- dualAugA
- dualAugB
- PrimalFeasible
- rowEval
