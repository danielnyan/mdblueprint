---
id: integralGreedy-halfApprox-dpOptimal
title: integralGreedy_halfApprox_dpOptimal
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - integralGreedy_halfApprox_dpOptimal
uses:
  - natAuctionData
  - fractionalFeasible
  - fractionalSocialWelfare
  - realBidOfNat
  - binaryToAllocation
  - fractionalSocialWelfare_realBidOfNat_binaryToAllocation
  - dynamicProgrammingOptimalAllocation_fractionalFeasible
  - natFractionalGreedyValue_le_integralGreedyValue_plus_highest
---

# integralGreedy_halfApprox_dpOptimal

## Lean type

```lean
theorem integralGreedy_halfApprox_dpOptimal (w b : I → Nat) (capacity : Nat) (hwpos : ∀ i, 0 < w i) (_hallfit : ∀ i, w i ≤ capacity) (hfracOptimal : ∀ x : I → ℝ, (natAuctionData w capacity).fractionalFeasible x → fractionalSocialWelfare (realBidOfNat b) x ≤ natFractionalGreedyValue w b capacity) : ((dynamicProgrammingOptimalValue w b capacity : ℝ) / 2) ≤ max (integralGreedyValue w b capacity) (highestBidValue b)
```

## Dependencies

- natAuctionData
- fractionalFeasible
- fractionalSocialWelfare
- realBidOfNat
- binaryToAllocation
- fractionalSocialWelfare_realBidOfNat_binaryToAllocation
- dynamicProgrammingOptimalAllocation_fractionalFeasible
- natFractionalGreedyValue_le_integralGreedyValue_plus_highest
