---
id: virtualSurplusMaximizingAuction-regularMyersonOptimalICIR-of-isRegular
title: virtualSurplusMaximizingAuction_regularMyersonOptimalICIR_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_regularMyersonOptimalICIR_of_isRegular
uses:
  - IsRegular
  - IsRegularMyersonOptimalICIRAuction
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - virtualSurplusMaximizingAuction_isIncentiveCompatible_and_individuallyRationalOnSupport_of_isRegular
  - virtualSurplusMaximizingAuction_allocationRule_isVirtualSurplusOptimal
  - virtualSurplusMaximizingAuction_isFeasible
  - virtualSurplusMaximizingAuction_isExpectedSellerRevenueOptimalInEnvironmentAmongFeasibleICIRIntegrable_of_isRegular
---

# virtualSurplusMaximizingAuction_regularMyersonOptimalICIR_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_regularMyersonOptimalICIR_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) (h : A.RegularMyersonICIRAnalyticAssumptions) : A.IsRegularMyersonOptimalICIRAuction A.virtualSurplusMaximizingAuction
```

## Dependencies

- IsRegular
- IsRegularMyersonOptimalICIRAuction
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- virtualSurplusMaximizingAuction_isIncentiveCompatible_and_individuallyRationalOnSupport_of_isRegular
- virtualSurplusMaximizingAuction_allocationRule_isVirtualSurplusOptimal
- virtualSurplusMaximizingAuction_isFeasible
- virtualSurplusMaximizingAuction_isExpectedSellerRevenueOptimalInEnvironmentAmongFeasibleICIRIntegrable_of_isRegular
