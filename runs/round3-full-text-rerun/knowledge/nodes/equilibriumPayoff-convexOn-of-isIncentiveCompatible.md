---
id: equilibriumPayoff-convexOn-of-isIncentiveCompatible
title: equilibriumPayoff_convexOn_of_isIncentiveCompatible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - equilibriumPayoff_convexOn_of_isIncentiveCompatible
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
---

# equilibriumPayoff_convexOn_of_isIncentiveCompatible

## Lean type

```lean
theorem equilibriumPayoff_convexOn_of_isIncentiveCompatible (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) (i : I) : ConvexOn ℝ Set.univ (A.equilibriumPayoff i)
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
