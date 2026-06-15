---
id: IsRevenueUpperBounded
title: IsRevenueUpperBounded
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsRevenueUpperBounded
uses:
  - HasSameSellingEnvironment
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - HasExpectedRevenueVirtualSurplusUpperBound
---

# IsRevenueUpperBounded

## Lean type

```lean
def IsRevenueUpperBounded [Fintype I] (A B : BayesianSingleItemAuction I) : Prop
```

## Dependencies

- HasSameSellingEnvironment
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- HasExpectedRevenueVirtualSurplusUpperBound
