---
id: hasInterimEnvelopeFormula-of-isIncentiveCompatible-of-hasInterimEnvelopeDerivative
title: hasInterimEnvelopeFormula_of_isIncentiveCompatible_of_hasInterimEnvelopeDerivative
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasInterimEnvelopeFormula_of_isIncentiveCompatible_of_hasInterimEnvelopeDerivative
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - HasInterimEnvelopeDerivative
  - HasInterimEnvelopeFormula
  - hasInterimEnvelopeFormula_of_hasInterimEnvelopeDerivative
  - hasIntervalIntegrableInterimAllocation_of_isIncentiveCompatible
---

# hasInterimEnvelopeFormula_of_isIncentiveCompatible_of_hasInterimEnvelopeDerivative

## Lean type

```lean
theorem hasInterimEnvelopeFormula_of_isIncentiveCompatible_of_hasInterimEnvelopeDerivative (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) (hderiv : A.HasInterimEnvelopeDerivative) : A.HasInterimEnvelopeFormula
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- HasInterimEnvelopeDerivative
- HasInterimEnvelopeFormula
- hasInterimEnvelopeFormula_of_hasInterimEnvelopeDerivative
- hasIntervalIntegrableInterimAllocation_of_isIncentiveCompatible
