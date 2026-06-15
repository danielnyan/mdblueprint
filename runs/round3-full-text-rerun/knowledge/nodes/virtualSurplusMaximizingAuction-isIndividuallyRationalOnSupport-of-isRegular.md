---
id: virtualSurplusMaximizingAuction-isIndividuallyRationalOnSupport-of-isRegular
title: virtualSurplusMaximizingAuction_isIndividuallyRationalOnSupport_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isIndividuallyRationalOnSupport_of_isRegular
uses:
  - IsRegular
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - virtualSurplusMaximizingAuction_isIncentiveCompatible_and_individuallyRationalOnSupport_of_isRegular
---

# virtualSurplusMaximizingAuction_isIndividuallyRationalOnSupport_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isIndividuallyRationalOnSupport_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : (A.virtualSurplusMaximizingAuction).IsIndividuallyRationalOnSupport
```

## Dependencies

- IsRegular
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- virtualSurplusMaximizingAuction_isIncentiveCompatible_and_individuallyRationalOnSupport_of_isRegular
