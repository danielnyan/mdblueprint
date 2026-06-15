---
id: hasInterimEnvelopeFormula-of-isIncentiveCompatible
title: hasInterimEnvelopeFormula_of_isIncentiveCompatible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasInterimEnvelopeFormula_of_isIncentiveCompatible
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - HasInterimEnvelopeFormula
  - equilibriumPayoff_convexOn_of_isIncentiveCompatible
  - deriv_equilibriumPayoff_eq_interimAllocProb_of_isIncentiveCompatible
---

# hasInterimEnvelopeFormula_of_isIncentiveCompatible

## Lean type

```lean
theorem hasInterimEnvelopeFormula_of_isIncentiveCompatible (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) : A.HasInterimEnvelopeFormula
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- HasInterimEnvelopeFormula
- equilibriumPayoff_convexOn_of_isIncentiveCompatible
- deriv_equilibriumPayoff_eq_interimAllocProb_of_isIncentiveCompatible
