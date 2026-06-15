---
id: virtualSurplusMaximizingAuction-allocationRule-isVirtualSurplusOptimal
title: virtualSurplusMaximizingAuction_allocationRule_isVirtualSurplusOptimal
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_allocationRule_isVirtualSurplusOptimal
uses:
  - IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
  - IsVirtualSurplusOptimalAllocationRule
  - virtualSurplusMaximizingAllocationRule_isVirtualSurplusOptimalAllocationRule
---

# virtualSurplusMaximizingAuction_allocationRule_isVirtualSurplusOptimal

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_allocationRule_isVirtualSurplusOptimal [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) : A.IsVirtualSurplusOptimalAllocationRule (A.virtualSurplusMaximizingAuction).allocationRule
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
- IsVirtualSurplusOptimalAllocationRule
- virtualSurplusMaximizingAllocationRule_isVirtualSurplusOptimalAllocationRule
