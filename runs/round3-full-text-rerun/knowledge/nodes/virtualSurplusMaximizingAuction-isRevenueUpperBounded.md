---
id: virtualSurplusMaximizingAuction-isRevenueUpperBounded
title: virtualSurplusMaximizingAuction_isRevenueUpperBounded
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isRevenueUpperBounded
uses:
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - HasExpectedRevenueVirtualSurplusIdentity
  - IsRevenueUpperBounded
  - isRevenueUpperBounded_of_isRevenueComparable
  - virtualSurplusMaximizingAuction_isRevenueComparable
---

# virtualSurplusMaximizingAuction_isRevenueUpperBounded

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isRevenueUpperBounded [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hopt_int : A.IntegrableVirtualSurplus (A.virtualSurplusMaximizingAuction).allocationRule) (hopt_id : A.HasExpectedRevenueVirtualSurplusIdentity A.virtualSurplusMaximizingAuction) : A.IsRevenueUpperBounded A.virtualSurplusMaximizingAuction
```

## Dependencies

- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- HasExpectedRevenueVirtualSurplusIdentity
- IsRevenueUpperBounded
- isRevenueUpperBounded_of_isRevenueComparable
- virtualSurplusMaximizingAuction_isRevenueComparable
