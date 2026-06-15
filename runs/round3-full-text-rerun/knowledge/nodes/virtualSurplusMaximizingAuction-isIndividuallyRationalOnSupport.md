---
id: virtualSurplusMaximizingAuction-isIndividuallyRationalOnSupport
title: virtualSurplusMaximizingAuction_isIndividuallyRationalOnSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isIndividuallyRationalOnSupport
uses:
  - HasInterimEnvelopeFormula
  - HasNonnegativeInterimAllocationIntegralOnSupport
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - isIndividuallyRationalOnSupport_of_isZeroNormalized_of_hasInterimEnvelopeFormula
  - virtualSurplusMaximizingAuction_isZeroNormalized
---

# virtualSurplusMaximizingAuction_isIndividuallyRationalOnSupport

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isIndividuallyRationalOnSupport [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (henv : A.virtualSurplusMaximizingAuction.HasInterimEnvelopeFormula) (hint_nonneg : A.virtualSurplusMaximizingAuction.HasNonnegativeInterimAllocationIntegralOnSupport) : (A.virtualSurplusMaximizingAuction).IsIndividuallyRationalOnSupport
```

## Dependencies

- HasInterimEnvelopeFormula
- HasNonnegativeInterimAllocationIntegralOnSupport
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- isIndividuallyRationalOnSupport_of_isZeroNormalized_of_hasInterimEnvelopeFormula
- virtualSurplusMaximizingAuction_isZeroNormalized
