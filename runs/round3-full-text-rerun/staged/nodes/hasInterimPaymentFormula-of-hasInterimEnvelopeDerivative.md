---
id: hasInterimPaymentFormula-of-hasInterimEnvelopeDerivative
title: hasInterimPaymentFormula_of_hasInterimEnvelopeDerivative
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasInterimPaymentFormula_of_hasInterimEnvelopeDerivative
uses:
  - HasInterimEnvelopeDerivative
  - HasIntervalIntegrableInterimAllocation
  - HasInterimPaymentFormula
  - hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
  - hasInterimEnvelopeFormula_of_hasInterimEnvelopeDerivative
---

# hasInterimPaymentFormula_of_hasInterimEnvelopeDerivative

## Lean type

```lean
theorem hasInterimPaymentFormula_of_hasInterimEnvelopeDerivative (A : BayesianSingleItemAuction I) (hderiv : A.HasInterimEnvelopeDerivative) (hint : A.HasIntervalIntegrableInterimAllocation) : A.HasInterimPaymentFormula
```

## Dependencies

- HasInterimEnvelopeDerivative
- HasIntervalIntegrableInterimAllocation
- HasInterimPaymentFormula
- hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
- hasInterimEnvelopeFormula_of_hasInterimEnvelopeDerivative
