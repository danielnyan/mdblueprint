---
id: natBinarySocialWelfare
title: natBinarySocialWelfare
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - natBinarySocialWelfare
uses:
  - BinaryAllocation
---

# natBinarySocialWelfare

## Lean type

```lean
def natBinarySocialWelfare (b : I → Nat) (x : BinaryAllocation I) : Nat
```

## Dependencies

- BinaryAllocation
