---
id: EnvelopeVirtualSurplusEnvironmentAssumptions-typeMeasure-isProbabilityMeasure
title: EnvelopeVirtualSurplusEnvironmentAssumptions.typeMeasure_isProbabilityMeasure
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - EnvelopeVirtualSurplusEnvironmentAssumptions.typeMeasure_isProbabilityMeasure
uses:
  - typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_positiveDensity
---

# EnvelopeVirtualSurplusEnvironmentAssumptions.typeMeasure_isProbabilityMeasure

## Lean type

```lean
theorem EnvelopeVirtualSurplusEnvironmentAssumptions.typeMeasure_isProbabilityMeasure {A : BayesianSingleItemAuction I} (h : A.EnvelopeVirtualSurplusEnvironmentAssumptions) (i : I) : IsProbabilityMeasure (A.typeMeasure i)
```

## Dependencies

- typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_positiveDensity
