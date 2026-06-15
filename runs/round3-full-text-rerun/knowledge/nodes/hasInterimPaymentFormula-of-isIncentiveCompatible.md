---
id: hasInterimPaymentFormula-of-isIncentiveCompatible
title: hasInterimPaymentFormula_of_isIncentiveCompatible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasInterimPaymentFormula_of_isIncentiveCompatible
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - HasInterimPaymentFormula
  - hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
  - hasInterimEnvelopeFormula_of_isIncentiveCompatible
---

# hasInterimPaymentFormula_of_isIncentiveCompatible

## Lean type

```lean
theorem hasInterimPaymentFormula_of_isIncentiveCompatible (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) : A.HasInterimPaymentFormula
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- HasInterimPaymentFormula
- hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
- hasInterimEnvelopeFormula_of_isIncentiveCompatible
