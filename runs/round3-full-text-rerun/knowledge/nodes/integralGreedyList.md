---
id: integralGreedyList
title: integralGreedyList
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - integralGreedyList
uses:
  - BinaryAllocation
  - natAuctionData
  - realBidOfNat
  - natBinarySocialWelfare
---

# integralGreedyList

## Lean type

```lean
def integralGreedyList (w : I → Nat) : List I → Nat → BinaryAllocation I | [], _ => fun _ => false | i :: items, remaining => if w i ≤ remaining then Function.update (integralGreedyList w items (remaining - w i)) i true else fun _ => false termination_by items _ => items.length /-- The ratio-sorted integral greedy allocation. -/ noncomputable def integralGreedyAllocation (w b : I → Nat) (capacity : Nat) : BinaryAllocation I
```

## Dependencies

- BinaryAllocation
- natAuctionData
- realBidOfNat
- natBinarySocialWelfare
