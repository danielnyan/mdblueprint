---
id: exists-reserveThreshold-le-bid-of-exists-virtualSurplusMaximizingAllocationRule-eq-one
title: exists_reserveThreshold_le_bid_of_exists_virtualSurplusMaximizingAllocationRule_eq_one
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - exists_reserveThreshold_le_bid_of_exists_virtualSurplusMaximizingAllocationRule_eq_one
uses:
  - IsReserveThreshold
  - reserveThreshold_le_bid_of_virtualSurplusMaximizingAllocationRule_eq_one
---

# exists_reserveThreshold_le_bid_of_exists_virtualSurplusMaximizingAllocationRule_eq_one

## Lean type

```lean
theorem exists_reserveThreshold_le_bid_of_exists_virtualSurplusMaximizingAllocationRule_eq_one [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {reserve b : I → ℝ} (hreserve : ∀ i, A.IsReserveThreshold i (reserve i)) (hsale : ∃ i, A.virtualSurplusMaximizingAllocationRule b i = 1) : ∃ i, reserve i ≤ b i
```

## Dependencies

- IsReserveThreshold
- reserveThreshold_le_bid_of_virtualSurplusMaximizingAllocationRule_eq_one
