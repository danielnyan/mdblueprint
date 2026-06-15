---
id: hasInterimPaymentFormula-of-hasInterimEnvelopeFormula
title: hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
uses:
  - HasInterimEnvelopeFormula
  - HasInterimPaymentFormula
---

# hasInterimPaymentFormula_of_hasInterimEnvelopeFormula

## Lean type

```lean
theorem hasInterimPaymentFormula_of_hasInterimEnvelopeFormula (A : BayesianSingleItemAuction I) (henv : A.HasInterimEnvelopeFormula) : A.HasInterimPaymentFormula
```

## Dependencies

- HasInterimEnvelopeFormula
- HasInterimPaymentFormula
