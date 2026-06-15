---
id: expectedSellerRevenueInEnvironment-le-virtualSurplusMaximizingAuction
title: expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction
uses:
  - IsRevenueComparable
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - HasExpectedRevenueVirtualSurplusIdentity
  - expectedSellerRevenueInEnvironment_le_of_expectedVirtualSurplus_le
  - expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_allocationRule
  - IsFeasible.isSingleItemAllocationRule
  - IsSingleItemAllocationRule
---

# expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction

## Lean type

```lean
theorem expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A B : BayesianSingleItemAuction I) (hB : A.IsRevenueComparable B) (hopt_int : A.IntegrableVirtualSurplus (A.virtualSurplusMaximizingAuction).allocationRule) (hopt_id : A.HasExpectedRevenueVirtualSurplusIdentity A.virtualSurplusMaximizingAuction) : A.expectedSellerRevenueInEnvironment B ≤ A.expectedSellerRevenueInEnvironment A.virtualSurplusMaximizingAuction
```

## Dependencies

- IsRevenueComparable
- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- HasExpectedRevenueVirtualSurplusIdentity
- expectedSellerRevenueInEnvironment_le_of_expectedVirtualSurplus_le
- expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_allocationRule
- IsFeasible.isSingleItemAllocationRule
- IsSingleItemAllocationRule
