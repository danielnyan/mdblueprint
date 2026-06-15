---
id: supportedOn-tail-of-eq-false
title: supportedOn_tail_of_eq_false
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - supportedOn_tail_of_eq_false
uses:
  - BinaryAllocation
  - supportedOn
---

# supportedOn_tail_of_eq_false

## Lean type

```lean
lemma supportedOn_tail_of_eq_false {i : I} {items : List I} {x : BinaryAllocation I} (hsupp : supportedOn (i :: items) x) (hxi : x i = false) : supportedOn items x
```

## Dependencies

- BinaryAllocation
- supportedOn
