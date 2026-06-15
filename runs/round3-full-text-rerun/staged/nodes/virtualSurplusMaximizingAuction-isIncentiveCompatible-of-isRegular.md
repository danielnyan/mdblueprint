---
id: virtualSurplusMaximizingAuction-isIncentiveCompatible-of-isRegular
title: virtualSurplusMaximizingAuction_isIncentiveCompatible_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isIncentiveCompatible_of_isRegular
uses:
  - IsRegular
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - HasIntegrableInterimObjects
  - virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_isRegular
  - isIncentiveCompatible_of_isDSIC
  - virtualSurplusMaximizingAuction_isDSIC_of_isRegular
---

# virtualSurplusMaximizingAuction_isIncentiveCompatible_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isIncentiveCompatible_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : (A.virtualSurplusMaximizingAuction).IsIncentiveCompatible
```

## Dependencies

- IsRegular
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- HasIntegrableInterimObjects
- virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_isRegular
- isIncentiveCompatible_of_isDSIC
- virtualSurplusMaximizingAuction_isDSIC_of_isRegular
