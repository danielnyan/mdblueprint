---
id: virtualSurplusMaximizingWinner-virtualValue-ge
title: virtualSurplusMaximizingWinner_virtualValue_ge
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingWinner_virtualValue_ge
uses:
  - bid_le_maxBid
---

# virtualSurplusMaximizingWinner_virtualValue_ge

## Lean type

```lean
theorem virtualSurplusMaximizingWinner_virtualValue_ge [Fintype I] [Nontrivial I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) (i : I) : A.virtualValue i (b i) ≤ A.winningVirtualValue b
```

## Dependencies

- bid_le_maxBid
