---
id: hasInterimEnvelopeFormula-of-hasInterimEnvelopeDerivative
title: hasInterimEnvelopeFormula_of_hasInterimEnvelopeDerivative
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasInterimEnvelopeFormula_of_hasInterimEnvelopeDerivative
uses:
  - HasInterimEnvelopeDerivative
  - HasIntervalIntegrableInterimAllocation
  - HasInterimEnvelopeFormula
---

# hasInterimEnvelopeFormula_of_hasInterimEnvelopeDerivative

## Lean type

```lean
theorem hasInterimEnvelopeFormula_of_hasInterimEnvelopeDerivative (A : BayesianSingleItemAuction I) (hderiv : A.HasInterimEnvelopeDerivative) (hint : A.HasIntervalIntegrableInterimAllocation) : A.HasInterimEnvelopeFormula
```

## Dependencies

- HasInterimEnvelopeDerivative
- HasIntervalIntegrableInterimAllocation
- HasInterimEnvelopeFormula
