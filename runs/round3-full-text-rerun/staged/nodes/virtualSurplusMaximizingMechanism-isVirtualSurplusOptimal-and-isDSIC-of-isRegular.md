---
id: virtualSurplusMaximizingMechanism-isVirtualSurplusOptimal-and-isDSIC-of-isRegular
title: virtualSurplusMaximizingMechanism_isVirtualSurplusOptimal_and_isDSIC_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingMechanism_isVirtualSurplusOptimal_and_isDSIC_of_isRegular
uses:
  - IsRegular
  - IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
  - IsVirtualSurplusOptimalAllocationRule
  - IsDSIC
  - isDSIC
  - virtualSurplusMaximizingMechanism_allocationRule_isVirtualSurplusOptimal
  - virtualSurplusMaximizingMechanism_isDSIC_of_isRegular
---

# virtualSurplusMaximizingMechanism_isVirtualSurplusOptimal_and_isDSIC_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingMechanism_isVirtualSurplusOptimal_and_isDSIC_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : A.IsVirtualSurplusOptimalAllocationRule (A.virtualSurplusMaximizingMechanism).allocationRule ∧ (A.virtualSurplusMaximizingMechanism).IsDSIC
```

## Dependencies

- IsRegular
- IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
- IsVirtualSurplusOptimalAllocationRule
- IsDSIC
- isDSIC
- virtualSurplusMaximizingMechanism_allocationRule_isVirtualSurplusOptimal
- virtualSurplusMaximizingMechanism_isDSIC_of_isRegular
