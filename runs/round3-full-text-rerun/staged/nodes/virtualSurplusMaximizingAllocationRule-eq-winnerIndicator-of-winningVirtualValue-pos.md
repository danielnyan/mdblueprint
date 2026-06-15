---
id: virtualSurplusMaximizingAllocationRule-eq-winnerIndicator-of-winningVirtualValue-pos
title: virtualSurplusMaximizingAllocationRule_eq_winnerIndicator_of_winningVirtualValue_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_eq_winnerIndicator_of_winningVirtualValue_pos
uses:
---

# virtualSurplusMaximizingAllocationRule_eq_winnerIndicator_of_winningVirtualValue_pos

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_eq_winnerIndicator_of_winningVirtualValue_pos [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) (hpos : 0 < A.winningVirtualValue b) : A.virtualSurplusMaximizingAllocationRule b = fun i => if i = A.virtualSurplusMaximizingWinner b then (1 : ℝ) else 0
```

## Dependencies

- none
