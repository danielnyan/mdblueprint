---
id: hasInterimPaymentEnvelopeUpperBound-of-isIncentiveCompatible-of-isIndividuallyRationalOnSupport
title: hasInterimPaymentEnvelopeUpperBound_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - hasInterimPaymentEnvelopeUpperBound_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - HasInterimPaymentEnvelopeUpperBound
  - hasInterimPaymentEnvelopeUpperBound_of_pointwise
  - interimExpectedPayment_le_alloc_mul_sub_integral_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport
---

# hasInterimPaymentEnvelopeUpperBound_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport

## Lean type

```lean
theorem hasInterimPaymentEnvelopeUpperBound_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport [Fintype I] (A B : BayesianSingleItemAuction I) (hdens_ae : ∀ i : I, ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) (hint_pay : ∀ i : I, IntervalIntegrable (fun v => B.interimExpectedPayment i v * A.typeDensity i v) volume 0 (A.typeData.omega i)) (hint_env : ∀ i : I, IntervalIntegrable (fun v => (B.interimAllocProb i v * v - ∫ z in 0..v, B.interimAllocProb i z) * A.typeDensity i v) volume 0 (A.typeData.omega i)) (hIC : B.IsIncentiveCompatible) (hIR : B.IsIndividuallyRationalOnSupport) : A.HasInterimPaymentEnvelopeUpperBound B
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- HasInterimPaymentEnvelopeUpperBound
- hasInterimPaymentEnvelopeUpperBound_of_pointwise
- interimExpectedPayment_le_alloc_mul_sub_integral_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport
