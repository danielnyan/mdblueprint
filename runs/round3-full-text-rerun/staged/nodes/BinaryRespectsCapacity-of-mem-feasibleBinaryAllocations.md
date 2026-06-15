---
id: BinaryRespectsCapacity-of-mem-feasibleBinaryAllocations
title: BinaryRespectsCapacity_of_mem_feasibleBinaryAllocations
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - BinaryRespectsCapacity_of_mem_feasibleBinaryAllocations
uses:
  - BinaryAllocation
  - binaryRespectsCapacity
---

# BinaryRespectsCapacity_of_mem_feasibleBinaryAllocations

## Lean type

```lean
lemma BinaryRespectsCapacity_of_mem_feasibleBinaryAllocations (A : KnapsackAuction I U) {x : BinaryAllocation I} (hx : x ∈ A.feasibleBinaryAllocations) : A.binaryRespectsCapacity x
```

## Dependencies

- BinaryAllocation
- binaryRespectsCapacity
