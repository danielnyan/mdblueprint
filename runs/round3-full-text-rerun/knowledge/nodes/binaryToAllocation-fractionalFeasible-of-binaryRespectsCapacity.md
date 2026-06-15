---
id: binaryToAllocation-fractionalFeasible-of-binaryRespectsCapacity
title: binaryToAllocation_fractionalFeasible_of_binaryRespectsCapacity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - binaryToAllocation_fractionalFeasible_of_binaryRespectsCapacity
uses:
  - BinaryAllocation
  - binaryRespectsCapacity
  - fractionalFeasible
  - binaryToAllocation
  - binaryLoad
---

# binaryToAllocation_fractionalFeasible_of_binaryRespectsCapacity

## Lean type

```lean
lemma binaryToAllocation_fractionalFeasible_of_binaryRespectsCapacity (A : KnapsackAuction I U) {x : BinaryAllocation I} (hx : A.binaryRespectsCapacity x) : A.fractionalFeasible (binaryToAllocation x)
```

## Dependencies

- BinaryAllocation
- binaryRespectsCapacity
- fractionalFeasible
- binaryToAllocation
- binaryLoad
