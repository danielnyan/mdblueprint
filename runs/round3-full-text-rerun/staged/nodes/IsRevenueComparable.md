---
id: IsRevenueComparable
title: IsRevenueComparable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsRevenueComparable
uses:
  - HasSameSellingEnvironment
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - HasExpectedRevenueVirtualSurplusIdentity
---

# IsRevenueComparable

## Lean type

```lean
def IsRevenueComparable [Fintype I] (A B : BayesianSingleItemAuction I) : Prop
```

## Dependencies

- HasSameSellingEnvironment
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- HasExpectedRevenueVirtualSurplusIdentity
