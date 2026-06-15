---
id: typeMeasureInterimFubiniAnalyticAssumptions-of-typeMeasure-fubini
title: typeMeasureInterimFubiniAnalyticAssumptions_of_typeMeasure_fubini
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - typeMeasureInterimFubiniAnalyticAssumptions_of_typeMeasure_fubini
uses:
  - typeDensity_measurable
  - typeDensity_ennreal_ofReal_aemeasurable
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
  - RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
---

# typeMeasureInterimFubiniAnalyticAssumptions_of_typeMeasure_fubini

## Lean type

```lean
theorem typeMeasureInterimFubiniAnalyticAssumptions_of_typeMeasure_fubini [Fintype I] {A B : BayesianSingleItemAuction I} (hdens_ae : ∀ i : I, ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) (hpay_int : ∀ i : I, Integrable (fun t => B.paymentRule t i) A.prior) (hvs_int : ∀ i : I, Integrable (fun t => B.allocationRule t i * A.virtualValue i (t i)) A.prior) (hpay_fubini : ∀ i : I, (∫ t, B.paymentRule t i ∂A.prior) = ∫ v, B.interimExpectedPayment i v ∂A.typeMeasure i) (hvs_fubini : ∀ i : I, (∫ t, B.allocationRule t i * A.virtualValue i (t i) ∂A.prior) = ∫ v, B.interimAllocProb i v * A.virtualValue i v ∂A.typeMeasure i) : A.TypeMeasureInterimFubiniAnalyticAssumptions B
```

## Dependencies

- typeDensity_measurable
- typeDensity_ennreal_ofReal_aemeasurable
- EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
- RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
