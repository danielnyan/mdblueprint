---
id: natFractionalGreedyValue-le-integralGreedyValue-plus-highest
title: natFractionalGreedyValue_le_integralGreedyValue_plus_highest
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - natFractionalGreedyValue_le_integralGreedyValue_plus_highest
uses:
  - natAuctionData
  - realBidOfNat
  - natFractionalGreedyList_le_integralGreedyList_plus_highest
---

# natFractionalGreedyValue_le_integralGreedyValue_plus_highest

## Lean type

```lean
lemma natFractionalGreedyValue_le_integralGreedyValue_plus_highest (w b : I → Nat) (capacity : Nat) (hwpos : ∀ i, 0 < w i) : natFractionalGreedyValue w b capacity ≤ integralGreedyValue w b capacity + highestBidValue b
```

## Dependencies

- natAuctionData
- realBidOfNat
- natFractionalGreedyList_le_integralGreedyList_plus_highest
