---
id: expectedSellerRevenueInEnvironment-le-virtualSurplusMaximizingAuction-of-revenueUpperBounded
title: expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction_of_revenueUpperBounded
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction_of_revenueUpperBounded
uses:
  - IsRevenueUpperBounded
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - HasExpectedRevenueVirtualSurplusIdentity
  - expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_allocationRule
  - IsFeasible.isSingleItemAllocationRule
  - IsSingleItemAllocationRule
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction_of_revenueUpperBounded

## Lean type

```lean
theorem expectedSellerRevenueInEnvironment_le_virtualSurplusMaximizingAuction_of_revenueUpperBounded [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A B : BayesianSingleItemAuction I) (hB : A.IsRevenueUpperBounded B) (hopt_int : A.IntegrableVirtualSurplus (A.virtualSurplusMaximizingAuction).allocationRule) (hopt_id : A.HasExpectedRevenueVirtualSurplusIdentity A.virtualSurplusMaximizingAuction) : A.expectedSellerRevenueInEnvironment B ≤ A.expectedSellerRevenueInEnvironment A.virtualSurplusMaximizingAuction
```

## Dependencies

- IsRevenueUpperBounded
- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- HasExpectedRevenueVirtualSurplusIdentity
- expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_allocationRule
- IsFeasible.isSingleItemAllocationRule
- IsSingleItemAllocationRule
- IsPositiveAffineOf.symm
- Indifferent.symm
