---
id: RegularMyersonICIRAnalyticAssumptions-candidate-typeMeasure-interim-fubini
title: RegularMyersonICIRAnalyticAssumptions.candidate_typeMeasure_interim_fubini
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - RegularMyersonICIRAnalyticAssumptions.candidate_typeMeasure_interim_fubini
uses:
  - HasSameSellingEnvironment
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeMeasure_isProbabilityMeasure
  - RegularMyersonICIRAnalyticAssumptions.typeMeasure_isProbabilityMeasure
  - typeMeasureInterimFubiniAnalyticAssumptions_of_independentTypePriors
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
  - RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
---

# RegularMyersonICIRAnalyticAssumptions.candidate_typeMeasure_interim_fubini

## Lean type

```lean
theorem RegularMyersonICIRAnalyticAssumptions.candidate_typeMeasure_interim_fubini [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] {A : BayesianSingleItemAuction I} (h : A.RegularMyersonICIRAnalyticAssumptions) (B : BayesianSingleItemAuction I) (henv : A.HasSameSellingEnvironment B) (hfeas : B.IsFeasible) (hIC : B.IsIncentiveCompatible) (hIR : B.IsIndividuallyRationalOnSupport) : A.TypeMeasureInterimFubiniAnalyticAssumptions B
```

## Dependencies

- HasSameSellingEnvironment
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- EnvelopeVirtualSurplusEnvironmentAssumptions.typeMeasure_isProbabilityMeasure
- RegularMyersonICIRAnalyticAssumptions.typeMeasure_isProbabilityMeasure
- typeMeasureInterimFubiniAnalyticAssumptions_of_independentTypePriors
- EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
- RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
