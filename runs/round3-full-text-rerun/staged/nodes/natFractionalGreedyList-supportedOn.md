---
id: natFractionalGreedyList-supportedOn
title: natFractionalGreedyList_supportedOn
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - natFractionalGreedyList_supportedOn
uses:
  - fractionalSupportedOn
---

# natFractionalGreedyList_supportedOn

## Lean type

```lean
lemma natFractionalGreedyList_supportedOn (w : I → Nat) : ∀ items remaining, fractionalSupportedOn items (natFractionalGreedyList w items remaining)
```

## Dependencies

- fractionalSupportedOn
