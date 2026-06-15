---
id: supportedOn-nil-iff
title: supportedOn_nil_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - supportedOn_nil_iff
uses:
  - BinaryAllocation
  - supportedOn
  - eq_false_of_supportedOn_of_not_mem
---

# supportedOn_nil_iff

## Lean type

```lean
lemma supportedOn_nil_iff {x : BinaryAllocation I} : supportedOn ([] : List I) x ↔ x = fun _ => false
```

## Dependencies

- BinaryAllocation
- supportedOn
- eq_false_of_supportedOn_of_not_mem
