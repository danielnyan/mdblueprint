---
id: fractionalGreedyWelfare-ge-zeroOneWelfare-of-optimal
title: fractionalGreedyWelfare_ge_zeroOneWelfare_of_optimal
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - fractionalGreedyWelfare_ge_zeroOneWelfare_of_optimal
uses:
  - fractionalFeasible
  - fractionalSocialWelfare
  - binaryToAllocation
  - binaryToAllocation_fractionalFeasible_of_binaryRespectsCapacity
  - BinaryRespectsCapacity_of_mem_feasibleBinaryAllocations
  - welfareMaximizer_mem_feasibleBinaryAllocations
  - binarySocialWelfare
---

# fractionalGreedyWelfare_ge_zeroOneWelfare_of_optimal

## Lean type

```lean
theorem fractionalGreedyWelfare_ge_zeroOneWelfare_of_optimal (A : KnapsackAuction I U) (b : I → U) (hW : 0 ≤ A.totalCapacity) (hgreedyOptimal : ∀ x : I → U, A.fractionalFeasible x → fractionalSocialWelfare b x ≤ fractionalSocialWelfare b (A.fractionalGreedyAllocation b)) : A.maximalSocialWelfare b hW ≤ fractionalSocialWelfare b (A.fractionalGreedyAllocation b)
```

## Dependencies

- fractionalFeasible
- fractionalSocialWelfare
- binaryToAllocation
- binaryToAllocation_fractionalFeasible_of_binaryRespectsCapacity
- BinaryRespectsCapacity_of_mem_feasibleBinaryAllocations
- welfareMaximizer_mem_feasibleBinaryAllocations
- binarySocialWelfare
