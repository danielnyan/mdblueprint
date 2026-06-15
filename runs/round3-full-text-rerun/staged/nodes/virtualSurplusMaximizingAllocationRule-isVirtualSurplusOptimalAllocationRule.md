---
id: virtualSurplusMaximizingAllocationRule-isVirtualSurplusOptimalAllocationRule
title: virtualSurplusMaximizingAllocationRule_isVirtualSurplusOptimalAllocationRule
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_isVirtualSurplusOptimalAllocationRule
uses:
  - IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
  - IsVirtualSurplusOptimalAllocationRule
  - virtualSurplusMaximizingAllocationRule_isSingleItemAllocationRule
  - virtualSurplus_le_virtualSurplusMaximizingAllocationRule
---

# virtualSurplusMaximizingAllocationRule_isVirtualSurplusOptimalAllocationRule

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_isVirtualSurplusOptimalAllocationRule [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) : A.IsVirtualSurplusOptimalAllocationRule A.virtualSurplusMaximizingAllocationRule
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
- IsVirtualSurplusOptimalAllocationRule
- virtualSurplusMaximizingAllocationRule_isSingleItemAllocationRule
- virtualSurplus_le_virtualSurplusMaximizingAllocationRule
