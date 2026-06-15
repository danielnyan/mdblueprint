---
id: hasInterimPaymentEnvelopeUpperBound-of-pointwise
title: hasInterimPaymentEnvelopeUpperBound_of_pointwise
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - hasInterimPaymentEnvelopeUpperBound_of_pointwise
uses:
  - HasInterimPaymentEnvelopeUpperBound
---

# hasInterimPaymentEnvelopeUpperBound_of_pointwise

## Lean type

```lean
theorem hasInterimPaymentEnvelopeUpperBound_of_pointwise [Fintype I] (A B : BayesianSingleItemAuction I) (hdens_ae : ∀ i : I, ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) (hint_pay : ∀ i : I, IntervalIntegrable (fun v => B.interimExpectedPayment i v * A.typeDensity i v) volume 0 (A.typeData.omega i)) (hint_env : ∀ i : I, IntervalIntegrable (fun v => (B.interimAllocProb i v * v - ∫ z in 0..v, B.interimAllocProb i z) * A.typeDensity i v) volume 0 (A.typeData.omega i)) (hpoint : ∀ (i : I) (v : ℝ), 0 ≤ v → v ≤ A.typeData.omega i → B.interimExpectedPayment i v ≤ B.interimAllocProb i v * v - ∫ z in 0..v, B.interimAllocProb i z) : A.HasInterimPaymentEnvelopeUpperBound B
```

## Dependencies

- HasInterimPaymentEnvelopeUpperBound
