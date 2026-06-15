---
id: RegularMyersonICIRAnalyticAssumptions-candidate-envelope-analytic
title: RegularMyersonICIRAnalyticAssumptions.candidate_envelope_analytic
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - RegularMyersonICIRAnalyticAssumptions.candidate_envelope_analytic
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - envelopeVirtualSurplusAnalyticAssumptions_of_environment
  - hasIntervalIntegrableInterimAllocation_of_isIncentiveCompatible
  - RegularMyersonICIRAnalyticAssumptions.candidate_allocation_survival_integrable
  - RegularMyersonICIRAnalyticAssumptions.candidate_interim_virtual_surplus_density_integrable
---

# RegularMyersonICIRAnalyticAssumptions.candidate_envelope_analytic

## Lean type

```lean
theorem RegularMyersonICIRAnalyticAssumptions.candidate_envelope_analytic [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] {A : BayesianSingleItemAuction I} (h : A.RegularMyersonICIRAnalyticAssumptions) (B : BayesianSingleItemAuction I) (hfeas : B.IsFeasible) (hIC : B.IsIncentiveCompatible) (hIR : B.IsIndividuallyRationalOnSupport) : A.EnvelopeVirtualSurplusAnalyticAssumptions B
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- envelopeVirtualSurplusAnalyticAssumptions_of_environment
- hasIntervalIntegrableInterimAllocation_of_isIncentiveCompatible
- RegularMyersonICIRAnalyticAssumptions.candidate_allocation_survival_integrable
- RegularMyersonICIRAnalyticAssumptions.candidate_interim_virtual_surplus_density_integrable
