---
id: IsRegularMyersonOptimalICIRAuction-isIndividuallyRationalOnSupport
title: IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
uses:
  - IsRegularMyersonOptimalICIRAuction
  - IsIndividuallyRationalOnSupport
---

# IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport

## Lean type

```lean
theorem IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport [Fintype I] {A B : BayesianSingleItemAuction I} (hB : A.IsRegularMyersonOptimalICIRAuction B) : B.IsIndividuallyRationalOnSupport
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction
- IsIndividuallyRationalOnSupport
