---
id: binaryLoad
title: binaryLoad
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - binaryLoad
uses:
  - BinaryAllocation
  - binaryToAllocation
---

# binaryLoad

## Lean type

```lean
def binaryLoad (A : KnapsackAuction I U) (x : BinaryAllocation I) : U
```

## Dependencies

- BinaryAllocation
- binaryToAllocation
