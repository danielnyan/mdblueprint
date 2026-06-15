---
id: virtualSurplusMaximizingAuction-isRevenueComparable
title: virtualSurplusMaximizingAuction_isRevenueComparable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isRevenueComparable
uses:
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - HasExpectedRevenueVirtualSurplusIdentity
  - IsRevenueComparable
  - virtualSurplusMaximizingAuction_isFeasible
---

# virtualSurplusMaximizingAuction_isRevenueComparable

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isRevenueComparable [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hopt_int : A.IntegrableVirtualSurplus (A.virtualSurplusMaximizingAuction).allocationRule) (hopt_id : A.HasExpectedRevenueVirtualSurplusIdentity A.virtualSurplusMaximizingAuction) : A.IsRevenueComparable A.virtualSurplusMaximizingAuction
```

## Dependencies

- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- HasExpectedRevenueVirtualSurplusIdentity
- IsRevenueComparable
- virtualSurplusMaximizingAuction_isFeasible
