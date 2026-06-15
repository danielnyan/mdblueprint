---
id: welfareMaximizingAllocationRule-isMonotone
title: welfareMaximizingAllocationRule_isMonotone
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - welfareMaximizingAllocationRule_isMonotone
uses:
  - IsMonotone
  - welfareMaximizer_mem_feasibleBinaryAllocations
  - binarySocialWelfare
  - welfareMaximizer_ge
  - binaryToAllocation
  - binarySocialWelfare_update
---

# welfareMaximizingAllocationRule_isMonotone

## Lean type

```lean
lemma welfareMaximizingAllocationRule_isMonotone (A : KnapsackAuction I ℝ) (hW : 0 ≤ A.totalCapacity) : SingleParameterMechanism.IsMonotone ({ allocationRule
```

## Dependencies

- IsMonotone
- welfareMaximizer_mem_feasibleBinaryAllocations
- binarySocialWelfare
- welfareMaximizer_ge
- binaryToAllocation
- binarySocialWelfare_update
