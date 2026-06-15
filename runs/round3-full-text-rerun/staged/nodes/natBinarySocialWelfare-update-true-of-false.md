---
id: natBinarySocialWelfare-update-true-of-false
title: natBinarySocialWelfare_update_true_of_false
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - natBinarySocialWelfare_update_true_of_false
uses:
  - BinaryAllocation
  - natBinarySocialWelfare
---

# natBinarySocialWelfare_update_true_of_false

## Lean type

```lean
lemma natBinarySocialWelfare_update_true_of_false (b : I → Nat) {x : BinaryAllocation I} {i : I} (hxi : x i = false) : natBinarySocialWelfare b (Function.update x i true) = b i + natBinarySocialWelfare b x
```

## Dependencies

- BinaryAllocation
- natBinarySocialWelfare
