---
id: natBinaryLoad-eq-add-of-true
title: natBinaryLoad_eq_add_of_true
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - natBinaryLoad_eq_add_of_true
uses:
  - BinaryAllocation
  - natBinaryLoad
---

# natBinaryLoad_eq_add_of_true

## Lean type

```lean
lemma natBinaryLoad_eq_add_of_true (w : I → Nat) {x : BinaryAllocation I} {i : I} (hxi : x i = true) : natBinaryLoad w x = w i + natBinaryLoad w (Function.update x i false)
```

## Dependencies

- BinaryAllocation
- natBinaryLoad
