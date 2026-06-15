---
id: feasibleBinaryAllocations-nonempty
title: feasibleBinaryAllocations_nonempty
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - feasibleBinaryAllocations_nonempty
uses:
  - zeroBinaryRespectsCapacity
---

# feasibleBinaryAllocations_nonempty

## Lean type

```lean
lemma feasibleBinaryAllocations_nonempty (A : KnapsackAuction I U) (hW : 0 ≤ A.totalCapacity) : A.feasibleBinaryAllocations ≠ []
```

## Dependencies

- zeroBinaryRespectsCapacity
