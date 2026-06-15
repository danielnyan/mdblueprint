---
id: interimEnvelopeFormula-and-paymentFormula-of-isIncentiveCompatible-of-hasInterimEnvelopeDerivative
title: interimEnvelopeFormula_and_paymentFormula_of_isIncentiveCompatible_of_hasInterimEnvelopeDerivative
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimEnvelopeFormula_and_paymentFormula_of_isIncentiveCompatible_of_hasInterimEnvelopeDerivative
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - HasInterimEnvelopeDerivative
  - HasInterimEnvelopeFormula
  - HasInterimPaymentFormula
  - hasInterimEnvelopeFormula_of_isIncentiveCompatible_of_hasInterimEnvelopeDerivative
  - hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
---

# interimEnvelopeFormula_and_paymentFormula_of_isIncentiveCompatible_of_hasInterimEnvelopeDerivative

## Lean type

```lean
theorem interimEnvelopeFormula_and_paymentFormula_of_isIncentiveCompatible_of_hasInterimEnvelopeDerivative (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) (hderiv : A.HasInterimEnvelopeDerivative) : A.HasInterimEnvelopeFormula ∧ A.HasInterimPaymentFormula
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- HasInterimEnvelopeDerivative
- HasInterimEnvelopeFormula
- HasInterimPaymentFormula
- hasInterimEnvelopeFormula_of_isIncentiveCompatible_of_hasInterimEnvelopeDerivative
- hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
