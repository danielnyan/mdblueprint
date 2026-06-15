---
id: RegularMyersonICIRAnalyticAssumptions-candidate-integrableVirtualSurplus
title: RegularMyersonICIRAnalyticAssumptions.candidate_integrableVirtualSurplus
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - RegularMyersonICIRAnalyticAssumptions.candidate_integrableVirtualSurplus
uses:
  - HasSameSellingEnvironment
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeMeasure_isProbabilityMeasure
  - RegularMyersonICIRAnalyticAssumptions.typeMeasure_isProbabilityMeasure
  - integrableVirtualSurplus_of_profileSplit_integrable_of_hasIndependentTypePriors
---

# RegularMyersonICIRAnalyticAssumptions.candidate_integrableVirtualSurplus

## Lean type

```lean
theorem RegularMyersonICIRAnalyticAssumptions.candidate_integrableVirtualSurplus [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] {A : BayesianSingleItemAuction I} (h : A.RegularMyersonICIRAnalyticAssumptions) (B : BayesianSingleItemAuction I) (henv : A.HasSameSellingEnvironment B) (hfeas : B.IsFeasible) (hIC : B.IsIncentiveCompatible) (hIR : B.IsIndividuallyRationalOnSupport) : A.IntegrableVirtualSurplus B.allocationRule
```

## Dependencies

- HasSameSellingEnvironment
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- EnvelopeVirtualSurplusEnvironmentAssumptions.typeMeasure_isProbabilityMeasure
- RegularMyersonICIRAnalyticAssumptions.typeMeasure_isProbabilityMeasure
- integrableVirtualSurplus_of_profileSplit_integrable_of_hasIndependentTypePriors
