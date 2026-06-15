---
id: binaryRespectsCapacity
title: binaryRespectsCapacity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - binaryRespectsCapacity
uses:
  - BinaryAllocation
  - binaryLoad
---

# binaryRespectsCapacity

## Lean type

```lean
def binaryRespectsCapacity (A : KnapsackAuction I U) (x : BinaryAllocation I) : Prop
```

## Dependencies

- BinaryAllocation
- binaryLoad
