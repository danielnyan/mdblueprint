---
id: IsRegularMyersonOptimalICIRAuction-isExpectedSellerRevenueOptimal
title: IsRegularMyersonOptimalICIRAuction.isExpectedSellerRevenueOptimal
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsRegularMyersonOptimalICIRAuction.isExpectedSellerRevenueOptimal
uses:
  - IsRegularMyersonOptimalICIRAuction
  - IsExpectedSellerRevenueOptimalInEnvironmentAmong
  - IsFeasibleICIRIntegrable
---

# IsRegularMyersonOptimalICIRAuction.isExpectedSellerRevenueOptimal

## Lean type

```lean
theorem IsRegularMyersonOptimalICIRAuction.isExpectedSellerRevenueOptimal [Fintype I] {A B : BayesianSingleItemAuction I} (hB : A.IsRegularMyersonOptimalICIRAuction B) : A.IsExpectedSellerRevenueOptimalInEnvironmentAmong B (fun C => A.IsFeasibleICIRIntegrable C)
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction
- IsExpectedSellerRevenueOptimalInEnvironmentAmong
- IsFeasibleICIRIntegrable
