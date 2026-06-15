---
id: dynamicProgrammingOptimalAllocation-feasible
title: dynamicProgrammingOptimalAllocation_feasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - dynamicProgrammingOptimalAllocation_feasible
uses:
  - natBinaryLoad
  - dpSolveList_feasible
---

# dynamicProgrammingOptimalAllocation_feasible

## Lean type

```lean
theorem dynamicProgrammingOptimalAllocation_feasible (w b : I → Nat) (capacity : Nat) : natBinaryLoad w (dynamicProgrammingOptimalAllocation w b capacity) ≤ capacity
```

## Dependencies

- natBinaryLoad
- dpSolveList_feasible
