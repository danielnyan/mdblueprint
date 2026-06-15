---
id: virtualSurplusMaximizingWinner-eq-iff-forall-virtualScore-le
title: virtualSurplusMaximizingWinner_eq_iff_forall_virtualScore_le
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingWinner_eq_iff_forall_virtualScore_le
uses:
  - bid_le_maxBid
  - toDirectBayesianMechanismWithTransfers
  - DirectBayesianMechanismWithTransfers
---

# virtualSurplusMaximizingWinner_eq_iff_forall_virtualScore_le

## Lean type

```lean
theorem virtualSurplusMaximizingWinner_eq_iff_forall_virtualScore_le [Fintype I] [Nontrivial I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) (i : I) : A.virtualSurplusMaximizingWinner b = i ↔ ∀ j, A.virtualScore b j ≤ A.virtualScore b i
```

## Dependencies

- bid_le_maxBid
- toDirectBayesianMechanismWithTransfers
- DirectBayesianMechanismWithTransfers
