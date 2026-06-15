---
id: virtualSurplusMaximizingAllocationRule-winner-eq-one-of-winningVirtualValue-pos
title: virtualSurplusMaximizingAllocationRule_winner_eq_one_of_winningVirtualValue_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_winner_eq_one_of_winningVirtualValue_pos
uses:
---

# virtualSurplusMaximizingAllocationRule_winner_eq_one_of_winningVirtualValue_pos

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_winner_eq_one_of_winningVirtualValue_pos [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) (hpos : 0 < A.winningVirtualValue b) : A.virtualSurplusMaximizingAllocationRule b (A.virtualSurplusMaximizingWinner b) = 1
```

## Dependencies

- none
