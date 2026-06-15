---
id: zeroBinaryRespectsCapacity
title: zeroBinaryRespectsCapacity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - zeroBinaryRespectsCapacity
uses:
  - binaryRespectsCapacity
  - binaryLoad
  - binaryToAllocation
---

# zeroBinaryRespectsCapacity

## Lean type

```lean
lemma zeroBinaryRespectsCapacity (A : KnapsackAuction I U) (hW : 0 ≤ A.totalCapacity) : A.binaryRespectsCapacity (fun _ => false)
```

## Dependencies

- binaryRespectsCapacity
- binaryLoad
- binaryToAllocation
