---
id: natBinaryLoad-update-true-of-false
title: natBinaryLoad_update_true_of_false
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - natBinaryLoad_update_true_of_false
uses:
  - BinaryAllocation
  - natBinaryLoad
---

# natBinaryLoad_update_true_of_false

## Lean type

```lean
lemma natBinaryLoad_update_true_of_false (w : I → Nat) {x : BinaryAllocation I} {i : I} (hxi : x i = false) : natBinaryLoad w (Function.update x i true) = w i + natBinaryLoad w x
```

## Dependencies

- BinaryAllocation
- natBinaryLoad
