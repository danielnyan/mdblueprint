---
id: virtualSurplus-virtualSurplusMaximizingAllocationRule-eq-max-winningVirtualValue-zero
title: virtualSurplus_virtualSurplusMaximizingAllocationRule_eq_max_winningVirtualValue_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplus_virtualSurplusMaximizingAllocationRule_eq_max_winningVirtualValue_zero
uses:
---

# virtualSurplus_virtualSurplusMaximizingAllocationRule_eq_max_winningVirtualValue_zero

## Lean type

```lean
theorem virtualSurplus_virtualSurplusMaximizingAllocationRule_eq_max_winningVirtualValue_zero [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) : A.virtualSurplus A.virtualSurplusMaximizingAllocationRule b = max (A.winningVirtualValue b) 0
```

## Dependencies

- none
