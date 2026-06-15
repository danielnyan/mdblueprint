---
id: virtualSurplusMaximizingAuction-isExpectedSellerRevenueOptimalInEnvironmentAmongRevenueComparable
title: virtualSurplusMaximizingAuction_isExpectedSellerRevenueOptimalInEnvironmentAmongRevenueComparable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isExpectedSellerRevenueOptimalInEnvironmentAmongRevenueComparable
uses:
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - HasExpectedRevenueVirtualSurplusIdentity
  - IsExpectedSellerRevenueOptimalInEnvironmentAmong
  - IsRevenueComparable
  - virtualSurplusMaximizingAuction_isRevenueComparable
  - expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction
---

# virtualSurplusMaximizingAuction_isExpectedSellerRevenueOptimalInEnvironmentAmongRevenueComparable

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isExpectedSellerRevenueOptimalInEnvironmentAmongRevenueComparable [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hopt_int : A.IntegrableVirtualSurplus (A.virtualSurplusMaximizingAuction).allocationRule) (hopt_id : A.HasExpectedRevenueVirtualSurplusIdentity A.virtualSurplusMaximizingAuction) : A.IsExpectedSellerRevenueOptimalInEnvironmentAmong A.virtualSurplusMaximizingAuction (fun B => A.IsRevenueComparable B)
```

## Dependencies

- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- HasExpectedRevenueVirtualSurplusIdentity
- IsExpectedSellerRevenueOptimalInEnvironmentAmong
- IsRevenueComparable
- virtualSurplusMaximizingAuction_isRevenueComparable
- expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction
