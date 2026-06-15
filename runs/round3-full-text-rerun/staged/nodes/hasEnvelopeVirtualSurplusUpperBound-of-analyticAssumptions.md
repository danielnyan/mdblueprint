---
id: hasEnvelopeVirtualSurplusUpperBound-of-analyticAssumptions
title: hasEnvelopeVirtualSurplusUpperBound_of_analyticAssumptions
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - hasEnvelopeVirtualSurplusUpperBound_of_analyticAssumptions
uses:
  - HasEnvelopeVirtualSurplusUpperBound
  - EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegral_eq_virtualSurplusIntegral
---

# hasEnvelopeVirtualSurplusUpperBound_of_analyticAssumptions

## Lean type

```lean
theorem hasEnvelopeVirtualSurplusUpperBound_of_analyticAssumptions [Fintype I] (A B : BayesianSingleItemAuction I) (h : A.EnvelopeVirtualSurplusAnalyticAssumptions B) : A.HasEnvelopeVirtualSurplusUpperBound B
```

## Dependencies

- HasEnvelopeVirtualSurplusUpperBound
- EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegral_eq_virtualSurplusIntegral
