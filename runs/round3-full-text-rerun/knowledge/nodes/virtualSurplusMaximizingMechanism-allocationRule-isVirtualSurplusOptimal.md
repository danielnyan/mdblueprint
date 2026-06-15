---
id: virtualSurplusMaximizingMechanism-allocationRule-isVirtualSurplusOptimal
title: virtualSurplusMaximizingMechanism_allocationRule_isVirtualSurplusOptimal
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingMechanism_allocationRule_isVirtualSurplusOptimal
uses:
  - IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
  - IsVirtualSurplusOptimalAllocationRule
  - virtualSurplusMaximizingAllocationRule_isVirtualSurplusOptimalAllocationRule
---

# virtualSurplusMaximizingMechanism_allocationRule_isVirtualSurplusOptimal

## Lean type

```lean
theorem virtualSurplusMaximizingMechanism_allocationRule_isVirtualSurplusOptimal [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) : A.IsVirtualSurplusOptimalAllocationRule (A.virtualSurplusMaximizingMechanism).allocationRule
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
- IsVirtualSurplusOptimalAllocationRule
- virtualSurplusMaximizingAllocationRule_isVirtualSurplusOptimalAllocationRule
