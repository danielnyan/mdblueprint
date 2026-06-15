---
id: IsRegularMyersonOptimalICIRAuction
title: IsRegularMyersonOptimalICIRAuction
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsRegularMyersonOptimalICIRAuction
uses:
  - IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
  - IsVirtualSurplusOptimalAllocationRule
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - IsExpectedSellerRevenueOptimalInEnvironmentAmong
  - IsFeasibleICIRIntegrable
---

# IsRegularMyersonOptimalICIRAuction

## Lean type

```lean
def IsRegularMyersonOptimalICIRAuction [Fintype I] (A B : BayesianSingleItemAuction I) : Prop
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
- IsVirtualSurplusOptimalAllocationRule
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- IsExpectedSellerRevenueOptimalInEnvironmentAmong
- IsFeasibleICIRIntegrable
