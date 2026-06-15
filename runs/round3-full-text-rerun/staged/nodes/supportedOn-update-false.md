---
id: supportedOn-update-false
title: supportedOn_update_false
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - supportedOn_update_false
uses:
  - BinaryAllocation
  - supportedOn
---

# supportedOn_update_false

## Lean type

```lean
lemma supportedOn_update_false {i : I} {items : List I} {x : BinaryAllocation I} (hsupp : supportedOn (i :: items) x) : supportedOn items (Function.update x i false)
```

## Dependencies

- BinaryAllocation
- supportedOn
