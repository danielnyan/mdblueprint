---
id: paymentInterimFubiniAssumptions-of-typeMeasure-fubini
title: paymentInterimFubiniAssumptions_of_typeMeasure_fubini
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - paymentInterimFubiniAssumptions_of_typeMeasure_fubini
uses:
  - integral_typeMeasure_eq_intervalIntegral_mul
---

# paymentInterimFubiniAssumptions_of_typeMeasure_fubini

## Lean type

```lean
theorem paymentInterimFubiniAssumptions_of_typeMeasure_fubini [Fintype I] {A B : BayesianSingleItemAuction I} (hdens_meas : ∀ i : I, AEMeasurable (fun v => ENNReal.ofReal (A.typeDensity i v)) (volume.restrict (Set.Ioc 0 (A.typeData.omega i)))) (hdens_ae : ∀ i : I, ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) (hpay_int : ∀ i : I, Integrable (fun t => B.paymentRule t i) A.prior) (hpay_fubini : ∀ i : I, (∫ t, B.paymentRule t i ∂A.prior) = ∫ v, B.interimExpectedPayment i v ∂A.typeMeasure i) : A.PaymentInterimFubiniAssumptions B
```

## Dependencies

- integral_typeMeasure_eq_intervalIntegral_mul
