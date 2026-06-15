---
id: RegularMyersonICIRAnalyticAssumptions-candidate-payment-envelope-upper
title: RegularMyersonICIRAnalyticAssumptions.candidate_payment_envelope_upper
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - RegularMyersonICIRAnalyticAssumptions.candidate_payment_envelope_upper
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - HasInterimPaymentEnvelopeUpperBound
  - hasInterimPaymentEnvelopeUpperBound_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
  - RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
  - RegularMyersonICIRAnalyticAssumptions.candidate_payment_density_integrable
  - RegularMyersonICIRAnalyticAssumptions.candidate_envelope_analytic
  - EnvelopeVirtualSurplusAnalyticAssumptions.envelope_density_integrable
---

# RegularMyersonICIRAnalyticAssumptions.candidate_payment_envelope_upper

## Lean type

```lean
theorem RegularMyersonICIRAnalyticAssumptions.candidate_payment_envelope_upper [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] {A B : BayesianSingleItemAuction I} (h : A.RegularMyersonICIRAnalyticAssumptions) (hfeas : B.IsFeasible) (hIC : B.IsIncentiveCompatible) (hIR : B.IsIndividuallyRationalOnSupport) : A.HasInterimPaymentEnvelopeUpperBound B
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- HasInterimPaymentEnvelopeUpperBound
- hasInterimPaymentEnvelopeUpperBound_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport
- EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
- RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
- RegularMyersonICIRAnalyticAssumptions.candidate_payment_density_integrable
- RegularMyersonICIRAnalyticAssumptions.candidate_envelope_analytic
- EnvelopeVirtualSurplusAnalyticAssumptions.envelope_density_integrable
