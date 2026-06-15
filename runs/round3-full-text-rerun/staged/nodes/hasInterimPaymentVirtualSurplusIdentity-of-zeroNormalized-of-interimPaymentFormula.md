---
id: hasInterimPaymentVirtualSurplusIdentity-of-zeroNormalized-of-interimPaymentFormula
title: hasInterimPaymentVirtualSurplusIdentity_of_zeroNormalized_of_interimPaymentFormula
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - hasInterimPaymentVirtualSurplusIdentity_of_zeroNormalized_of_interimPaymentFormula
uses:
  - IsZeroNormalized
  - HasInterimPaymentFormula
  - hasInterimPaymentEnvelopeIdentity_of_zeroNormalized_of_interimPaymentFormula
  - EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegral_eq_virtualSurplusIntegral
---

# hasInterimPaymentVirtualSurplusIdentity_of_zeroNormalized_of_interimPaymentFormula

## Lean type

```lean
theorem hasInterimPaymentVirtualSurplusIdentity_of_zeroNormalized_of_interimPaymentFormula [Fintype I] [DecidableEq I] (A B : BayesianSingleItemAuction I) (hzero : B.IsZeroNormalized) (hpay_formula : B.HasInterimPaymentFormula) (henv : A.EnvelopeVirtualSurplusAnalyticAssumptions B) : ∀ i : I, (∫ v in 0..A.typeData.omega i, B.interimExpectedPayment i v * A.typeDensity i v) = ∫ v in 0..A.typeData.omega i, B.interimAllocProb i v * A.virtualValue i v * A.typeDensity i v
```

## Dependencies

- IsZeroNormalized
- HasInterimPaymentFormula
- hasInterimPaymentEnvelopeIdentity_of_zeroNormalized_of_interimPaymentFormula
- EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegral_eq_virtualSurplusIntegral
