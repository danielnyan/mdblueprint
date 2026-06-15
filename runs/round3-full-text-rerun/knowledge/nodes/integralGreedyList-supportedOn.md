---
id: integralGreedyList-supportedOn
title: integralGreedyList_supportedOn
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - integralGreedyList_supportedOn
uses:
  - supportedOn
  - integralGreedyList
---

# integralGreedyList_supportedOn

## Lean type

```lean
lemma integralGreedyList_supportedOn (w : I → Nat) : ∀ items remaining, supportedOn items (integralGreedyList w items remaining)
```

## Dependencies

- supportedOn
- integralGreedyList
