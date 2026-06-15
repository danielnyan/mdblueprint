---
id: natBinarySocialWelfare-eq-add-of-true
title: natBinarySocialWelfare_eq_add_of_true
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - natBinarySocialWelfare_eq_add_of_true
uses:
  - BinaryAllocation
  - natBinarySocialWelfare
---

# natBinarySocialWelfare_eq_add_of_true

## Lean type

```lean
lemma natBinarySocialWelfare_eq_add_of_true (b : I → Nat) {x : BinaryAllocation I} {i : I} (hxi : x i = true) : natBinarySocialWelfare b x = b i + natBinarySocialWelfare b (Function.update x i false)
```

## Dependencies

- BinaryAllocation
- natBinarySocialWelfare
