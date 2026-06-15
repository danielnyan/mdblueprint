---
id: welfareMaximizer-mem-feasibleBinaryAllocations
title: welfareMaximizer_mem_feasibleBinaryAllocations
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - welfareMaximizer_mem_feasibleBinaryAllocations
uses:
  - exists_welfareMaximizer
---

# welfareMaximizer_mem_feasibleBinaryAllocations

## Lean type

```lean
lemma welfareMaximizer_mem_feasibleBinaryAllocations (A : KnapsackAuction I U) (b : I → U) (hW : 0 ≤ A.totalCapacity) : A.welfareMaximizer b hW ∈ A.feasibleBinaryAllocations
```

## Dependencies

- exists_welfareMaximizer
