---
id: exists-welfareMaximizer
title: exists_welfareMaximizer
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - exists_welfareMaximizer
uses:
  - BinaryAllocation
  - binarySocialWelfare
  - feasibleBinaryAllocations_nonempty
  - IsZeroSum.head
  - Subtree.head
  - exists_argMax_on
---

# exists_welfareMaximizer

## Lean type

```lean
lemma exists_welfareMaximizer (A : KnapsackAuction I U) (b : I → U) (hW : 0 ≤ A.totalCapacity) : ∃ x : BinaryAllocation I, x ∈ A.feasibleBinaryAllocations ∧ ∀ y ∈ A.feasibleBinaryAllocations, binarySocialWelfare b y ≤ binarySocialWelfare b x
```

## Dependencies

- BinaryAllocation
- binarySocialWelfare
- feasibleBinaryAllocations_nonempty
- IsZeroSum.head
- Subtree.head
- exists_argMax_on
