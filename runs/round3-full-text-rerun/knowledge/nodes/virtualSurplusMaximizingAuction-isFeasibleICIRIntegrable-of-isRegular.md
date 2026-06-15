---
id: virtualSurplusMaximizingAuction-isFeasibleICIRIntegrable-of-isRegular
title: virtualSurplusMaximizingAuction_isFeasibleICIRIntegrable_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isFeasibleICIRIntegrable_of_isRegular
uses:
  - IsRegular
  - IsFeasibleICIRIntegrable
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - virtualSurplusMaximizingAuction_isIncentiveCompatible_and_individuallyRationalOnSupport_of_isRegular
  - virtualSurplusMaximizingAuction_isFeasible
  - RegularMyersonICIRAnalyticAssumptions.candidate_integrableVirtualSurplus
---

# virtualSurplusMaximizingAuction_isFeasibleICIRIntegrable_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isFeasibleICIRIntegrable_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) (h : A.RegularMyersonICIRAnalyticAssumptions) : A.IsFeasibleICIRIntegrable A.virtualSurplusMaximizingAuction
```

## Dependencies

- IsRegular
- IsFeasibleICIRIntegrable
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- virtualSurplusMaximizingAuction_isIncentiveCompatible_and_individuallyRationalOnSupport_of_isRegular
- virtualSurplusMaximizingAuction_isFeasible
- RegularMyersonICIRAnalyticAssumptions.candidate_integrableVirtualSurplus
