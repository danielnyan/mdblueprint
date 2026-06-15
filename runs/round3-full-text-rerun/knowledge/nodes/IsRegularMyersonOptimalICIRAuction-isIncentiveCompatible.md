---
id: IsRegularMyersonOptimalICIRAuction-isIncentiveCompatible
title: IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
uses:
  - IsRegularMyersonOptimalICIRAuction
  - IsIncentiveCompatible
---

# IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible

## Lean type

```lean
theorem IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible [Fintype I] {A B : BayesianSingleItemAuction I} (hB : A.IsRegularMyersonOptimalICIRAuction B) : B.IsIncentiveCompatible
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction
- IsIncentiveCompatible
