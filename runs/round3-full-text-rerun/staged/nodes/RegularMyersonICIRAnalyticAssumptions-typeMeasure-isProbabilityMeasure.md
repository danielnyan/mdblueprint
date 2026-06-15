---
id: RegularMyersonICIRAnalyticAssumptions-typeMeasure-isProbabilityMeasure
title: RegularMyersonICIRAnalyticAssumptions.typeMeasure_isProbabilityMeasure
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - RegularMyersonICIRAnalyticAssumptions.typeMeasure_isProbabilityMeasure
uses:
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeMeasure_isProbabilityMeasure
---

# RegularMyersonICIRAnalyticAssumptions.typeMeasure_isProbabilityMeasure

## Lean type

```lean
theorem RegularMyersonICIRAnalyticAssumptions.typeMeasure_isProbabilityMeasure [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] {A : BayesianSingleItemAuction I} (h : A.RegularMyersonICIRAnalyticAssumptions) (i : I) : IsProbabilityMeasure (A.typeMeasure i)
```

## Dependencies

- EnvelopeVirtualSurplusEnvironmentAssumptions.typeMeasure_isProbabilityMeasure
