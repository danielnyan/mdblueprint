---
id: eq-false-of-supportedOn-of-not-mem
title: eq_false_of_supportedOn_of_not_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - eq_false_of_supportedOn_of_not_mem
uses:
  - BinaryAllocation
  - supportedOn
---

# eq_false_of_supportedOn_of_not_mem

## Lean type

```lean
lemma eq_false_of_supportedOn_of_not_mem {items : List I} {x : BinaryAllocation I} (hsupp : supportedOn items x) {i : I} (hi : i ∉ items) : x i = false
```

## Dependencies

- BinaryAllocation
- supportedOn
