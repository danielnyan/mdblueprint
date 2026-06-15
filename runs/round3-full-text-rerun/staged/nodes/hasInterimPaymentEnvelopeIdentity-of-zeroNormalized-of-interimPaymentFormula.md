---
id: hasInterimPaymentEnvelopeIdentity-of-zeroNormalized-of-interimPaymentFormula
title: hasInterimPaymentEnvelopeIdentity_of_zeroNormalized_of_interimPaymentFormula
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - hasInterimPaymentEnvelopeIdentity_of_zeroNormalized_of_interimPaymentFormula
uses:
  - IsZeroNormalized
  - HasInterimPaymentFormula
  - interimExpectedPayment_zero_of_isZeroNormalized
---

# hasInterimPaymentEnvelopeIdentity_of_zeroNormalized_of_interimPaymentFormula

## Lean type

```lean
theorem hasInterimPaymentEnvelopeIdentity_of_zeroNormalized_of_interimPaymentFormula [Fintype I] [DecidableEq I] (A B : BayesianSingleItemAuction I) (hzero : B.IsZeroNormalized) (hpay_formula : B.HasInterimPaymentFormula) : ∀ i : I, (∫ v in 0..A.typeData.omega i, B.interimExpectedPayment i v * A.typeDensity i v) = ∫ v in 0..A.typeData.omega i, (B.interimAllocProb i v * v - ∫ z in 0..v, B.interimAllocProb i z) * A.typeDensity i v
```

## Dependencies

- IsZeroNormalized
- HasInterimPaymentFormula
- interimExpectedPayment_zero_of_isZeroNormalized
