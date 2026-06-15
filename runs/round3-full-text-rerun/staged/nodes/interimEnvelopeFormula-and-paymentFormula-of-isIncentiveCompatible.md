---
id: interimEnvelopeFormula-and-paymentFormula-of-isIncentiveCompatible
title: interimEnvelopeFormula_and_paymentFormula_of_isIncentiveCompatible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimEnvelopeFormula_and_paymentFormula_of_isIncentiveCompatible
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - HasInterimEnvelopeFormula
  - HasInterimPaymentFormula
  - hasInterimEnvelopeFormula_of_isIncentiveCompatible
  - hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
---

# interimEnvelopeFormula_and_paymentFormula_of_isIncentiveCompatible

## Lean type

```lean
theorem interimEnvelopeFormula_and_paymentFormula_of_isIncentiveCompatible (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) : A.HasInterimEnvelopeFormula ∧ A.HasInterimPaymentFormula
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- HasInterimEnvelopeFormula
- HasInterimPaymentFormula
- hasInterimEnvelopeFormula_of_isIncentiveCompatible
- hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
