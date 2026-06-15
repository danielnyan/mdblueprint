---
id: virtualSurplusMaximizingAuction-isExpectedSellerRevenueOptimalInEnvironmentAmongRevenueUpperBounded
title: virtualSurplusMaximizingAuction_isExpectedSellerRevenueOptimalInEnvironmentAmongRevenueUpperBounded
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isExpectedSellerRevenueOptimalInEnvironmentAmongRevenueUpperBounded
uses:
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - HasExpectedRevenueVirtualSurplusIdentity
  - IsExpectedSellerRevenueOptimalInEnvironmentAmong
  - IsRevenueUpperBounded
  - virtualSurplusMaximizingAuction_isRevenueUpperBounded
  - expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction_of_revenueUpperBounded
---

# virtualSurplusMaximizingAuction_isExpectedSellerRevenueOptimalInEnvironmentAmongRevenueUpperBounded

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isExpectedSellerRevenueOptimalInEnvironmentAmongRevenueUpperBounded [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hopt_int : A.IntegrableVirtualSurplus (A.virtualSurplusMaximizingAuction).allocationRule) (hopt_id : A.HasExpectedRevenueVirtualSurplusIdentity A.virtualSurplusMaximizingAuction) : A.IsExpectedSellerRevenueOptimalInEnvironmentAmong A.virtualSurplusMaximizingAuction (fun B => A.IsRevenueUpperBounded B)
```

## Dependencies

- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- HasExpectedRevenueVirtualSurplusIdentity
- IsExpectedSellerRevenueOptimalInEnvironmentAmong
- IsRevenueUpperBounded
- virtualSurplusMaximizingAuction_isRevenueUpperBounded
- expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction_of_revenueUpperBounded
