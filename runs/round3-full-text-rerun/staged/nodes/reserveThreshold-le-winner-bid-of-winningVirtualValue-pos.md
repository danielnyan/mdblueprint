---
id: reserveThreshold-le-winner-bid-of-winningVirtualValue-pos
title: reserveThreshold_le_winner_bid_of_winningVirtualValue_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - reserveThreshold_le_winner_bid_of_winningVirtualValue_pos
uses:
  - IsReserveThreshold
  - reserveThreshold_le_bid_of_virtualSurplusMaximizingAllocationRule_eq_one
  - virtualSurplusMaximizingAllocationRule_winner_eq_one_of_winningVirtualValue_pos
---

# reserveThreshold_le_winner_bid_of_winningVirtualValue_pos

## Lean type

```lean
theorem reserveThreshold_le_winner_bid_of_winningVirtualValue_pos [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {reserve b : I → ℝ} (hreserve : ∀ i, A.IsReserveThreshold i (reserve i)) (hpos : 0 < A.winningVirtualValue b) : reserve (A.virtualSurplusMaximizingWinner b) ≤ b (A.virtualSurplusMaximizingWinner b)
```

## Dependencies

- IsReserveThreshold
- reserveThreshold_le_bid_of_virtualSurplusMaximizingAllocationRule_eq_one
- virtualSurplusMaximizingAllocationRule_winner_eq_one_of_winningVirtualValue_pos
