---
id: welfareMaximizer-ge
title: welfareMaximizer_ge
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - welfareMaximizer_ge
uses:
  - BinaryAllocation
  - binarySocialWelfare
  - exists_welfareMaximizer
---

# welfareMaximizer_ge

## Lean type

```lean
lemma welfareMaximizer_ge (A : KnapsackAuction I U) (b : I → U) (hW : 0 ≤ A.totalCapacity) {x : BinaryAllocation I} (hx : x ∈ A.feasibleBinaryAllocations) : binarySocialWelfare b x ≤ binarySocialWelfare b (A.welfareMaximizer b hW)
```

## Dependencies

- BinaryAllocation
- binarySocialWelfare
- exists_welfareMaximizer
