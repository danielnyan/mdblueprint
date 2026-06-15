---
id: virtualSurplusMaximizingAuction-isIncentiveCompatible-and-individuallyRationalOnSupport-of-isRegular
title: virtualSurplusMaximizingAuction_isIncentiveCompatible_and_individuallyRationalOnSupport_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isIncentiveCompatible_and_individuallyRationalOnSupport_of_isRegular
uses:
  - IsRegular
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - virtualSurplusMaximizingAuction_isIncentiveCompatible_of_isRegular
  - HasInterimEnvelopeFormula
  - hasInterimEnvelopeFormula_of_isIncentiveCompatible
  - HasNonnegativeInterimAllocationIntegralOnSupport
  - hasNonnegativeInterimAllocationIntegralOnSupport_of_isFeasible
  - virtualSurplusMaximizingAuction_isFeasible
  - virtualSurplusMaximizingAuction_isIndividuallyRationalOnSupport
---

# virtualSurplusMaximizingAuction_isIncentiveCompatible_and_individuallyRationalOnSupport_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isIncentiveCompatible_and_individuallyRationalOnSupport_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : (A.virtualSurplusMaximizingAuction).IsIncentiveCompatible ∧ (A.virtualSurplusMaximizingAuction).IsIndividuallyRationalOnSupport
```

## Dependencies

- IsRegular
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- virtualSurplusMaximizingAuction_isIncentiveCompatible_of_isRegular
- HasInterimEnvelopeFormula
- hasInterimEnvelopeFormula_of_isIncentiveCompatible
- HasNonnegativeInterimAllocationIntegralOnSupport
- hasNonnegativeInterimAllocationIntegralOnSupport_of_isFeasible
- virtualSurplusMaximizingAuction_isFeasible
- virtualSurplusMaximizingAuction_isIndividuallyRationalOnSupport
