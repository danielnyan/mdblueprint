---
id: virtualSurplusMaximizingAuction-isVirtualSurplusOptimal-and-isFeasible-and-isDSIC-of-isRegular
title: virtualSurplusMaximizingAuction_isVirtualSurplusOptimal_and_isFeasible_and_isDSIC_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isVirtualSurplusOptimal_and_isFeasible_and_isDSIC_of_isRegular
uses:
  - IsRegular
  - IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
  - IsVirtualSurplusOptimalAllocationRule
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsDSIC
  - isDSIC
  - virtualSurplusMaximizingAuction_allocationRule_isVirtualSurplusOptimal
  - virtualSurplusMaximizingAuction_isFeasible
  - virtualSurplusMaximizingAuction_isDSIC_of_isRegular
---

# virtualSurplusMaximizingAuction_isVirtualSurplusOptimal_and_isFeasible_and_isDSIC_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isVirtualSurplusOptimal_and_isFeasible_and_isDSIC_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : A.IsVirtualSurplusOptimalAllocationRule (A.virtualSurplusMaximizingAuction).allocationRule ∧ (A.virtualSurplusMaximizingAuction).IsFeasible ∧ (A.virtualSurplusMaximizingAuction).IsDSIC
```

## Dependencies

- IsRegular
- IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
- IsVirtualSurplusOptimalAllocationRule
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsDSIC
- isDSIC
- virtualSurplusMaximizingAuction_allocationRule_isVirtualSurplusOptimal
- virtualSurplusMaximizingAuction_isFeasible
- virtualSurplusMaximizingAuction_isDSIC_of_isRegular
