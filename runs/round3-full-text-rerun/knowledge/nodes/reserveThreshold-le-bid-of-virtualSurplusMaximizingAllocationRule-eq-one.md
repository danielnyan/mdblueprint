---
id: reserveThreshold-le-bid-of-virtualSurplusMaximizingAllocationRule-eq-one
title: reserveThreshold_le_bid_of_virtualSurplusMaximizingAllocationRule_eq_one
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - reserveThreshold_le_bid_of_virtualSurplusMaximizingAllocationRule_eq_one
uses:
  - IsReserveThreshold
  - virtualValue_pos_of_virtualSurplusMaximizingAllocationRule_eq_one
  - virtualValue_nonpos_of_lt_isReserveThreshold
---

# reserveThreshold_le_bid_of_virtualSurplusMaximizingAllocationRule_eq_one

## Lean type

```lean
theorem reserveThreshold_le_bid_of_virtualSurplusMaximizingAllocationRule_eq_one [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {b : I → ℝ} {i : I} {reserve : ℝ} (hreserve : A.IsReserveThreshold i reserve) (hi : A.virtualSurplusMaximizingAllocationRule b i = 1) : reserve ≤ b i
```

## Dependencies

- IsReserveThreshold
- virtualValue_pos_of_virtualSurplusMaximizingAllocationRule_eq_one
- virtualValue_nonpos_of_lt_isReserveThreshold
