---
id: dynamicProgrammingOptimalAllocation-optimal
title: dynamicProgrammingOptimalAllocation_optimal
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - dynamicProgrammingOptimalAllocation_optimal
uses:
  - BinaryAllocation
  - natBinaryLoad
  - natBinarySocialWelfare
  - dpSolveList_optimal
---

# dynamicProgrammingOptimalAllocation_optimal

## Lean type

```lean
theorem dynamicProgrammingOptimalAllocation_optimal (w b : I → Nat) (capacity : Nat) {x : BinaryAllocation I} (hfeas : natBinaryLoad w x ≤ capacity) : natBinarySocialWelfare b x ≤ natBinarySocialWelfare b (dynamicProgrammingOptimalAllocation w b capacity)
```

## Dependencies

- BinaryAllocation
- natBinaryLoad
- natBinarySocialWelfare
- dpSolveList_optimal
