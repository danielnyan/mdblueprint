---
id: exists-reserveThreshold-le-bid-of-winningVirtualValue-pos
title: exists_reserveThreshold_le_bid_of_winningVirtualValue_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - exists_reserveThreshold_le_bid_of_winningVirtualValue_pos
uses:
  - IsReserveThreshold
  - reserveThreshold_le_winner_bid_of_winningVirtualValue_pos
---

# exists_reserveThreshold_le_bid_of_winningVirtualValue_pos

## Lean type

```lean
theorem exists_reserveThreshold_le_bid_of_winningVirtualValue_pos [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {reserve b : I → ℝ} (hreserve : ∀ i, A.IsReserveThreshold i (reserve i)) (hpos : 0 < A.winningVirtualValue b) : ∃ i, reserve i ≤ b i
```

## Dependencies

- IsReserveThreshold
- reserveThreshold_le_winner_bid_of_winningVirtualValue_pos
