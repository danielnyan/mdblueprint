---
id: IsRegularMyersonOptimalICIRAuction-isFeasible
title: IsRegularMyersonOptimalICIRAuction.isFeasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsRegularMyersonOptimalICIRAuction.isFeasible
uses:
  - IsRegularMyersonOptimalICIRAuction
  - IsFeasible
---

# IsRegularMyersonOptimalICIRAuction.isFeasible

## Lean type

```lean
theorem IsRegularMyersonOptimalICIRAuction.isFeasible [Fintype I] {A B : BayesianSingleItemAuction I} (hB : A.IsRegularMyersonOptimalICIRAuction B) : B.IsFeasible
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction
- IsFeasible
