---
id: RegularMyersonICIRAnalyticAssumptions-candidate-payment-density-integrable
title: RegularMyersonICIRAnalyticAssumptions.candidate_payment_density_integrable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - RegularMyersonICIRAnalyticAssumptions.candidate_payment_density_integrable
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - intervalIntegrable_interimExpectedPayment_mul_typeDensity_of_profileSplit_integrable
  - typeDensity_ennreal_ofReal_aemeasurable
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
  - RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
---

# RegularMyersonICIRAnalyticAssumptions.candidate_payment_density_integrable

## Lean type

```lean
theorem RegularMyersonICIRAnalyticAssumptions.candidate_payment_density_integrable [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] {A : BayesianSingleItemAuction I} (h : A.RegularMyersonICIRAnalyticAssumptions) (B : BayesianSingleItemAuction I) (hfeas : B.IsFeasible) (hIC : B.IsIncentiveCompatible) (hIR : B.IsIndividuallyRationalOnSupport) : ∀ i : I, IntervalIntegrable (fun v => B.interimExpectedPayment i v * A.typeDensity i v) volume 0 (A.typeData.omega i)
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- intervalIntegrable_interimExpectedPayment_mul_typeDensity_of_profileSplit_integrable
- typeDensity_ennreal_ofReal_aemeasurable
- EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
- RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
