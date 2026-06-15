---
id: binarySocialWelfare
title: binarySocialWelfare
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - binarySocialWelfare
uses:
  - BinaryAllocation
  - binaryToAllocation
---

# binarySocialWelfare

## Lean type

```lean
def binarySocialWelfare (b : I → U) (x : BinaryAllocation I) : U
```

## Dependencies

- BinaryAllocation
- binaryToAllocation
