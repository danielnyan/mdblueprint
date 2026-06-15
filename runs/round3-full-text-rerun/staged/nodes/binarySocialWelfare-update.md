---
id: binarySocialWelfare-update
title: binarySocialWelfare_update
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - binarySocialWelfare_update
uses:
  - BinaryAllocation
  - binarySocialWelfare
  - binaryToAllocation
---

# binarySocialWelfare_update

## Lean type

```lean
lemma binarySocialWelfare_update (b : I → U) (i : I) (θ : U) (x : BinaryAllocation I) : binarySocialWelfare (Function.update b i θ) x = θ * binaryToAllocation x i + Finset.sum (Finset.univ.erase i) (fun j => b j * binaryToAllocation x j)
```

## Dependencies

- BinaryAllocation
- binarySocialWelfare
- binaryToAllocation
