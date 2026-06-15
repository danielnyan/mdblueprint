---
id: typeMeasure-isProbabilityMeasure-of-cdf-absolutelyContinuous-of-positiveDensity
title: typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_positiveDensity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_positiveDensity
uses:
  - HasPositiveDensityOnSupport
  - typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_density_nonnegative_ae
  - typeDensity_nonnegative_ae_of_hasPositiveDensityOnSupport
---

# typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_positiveDensity

## Lean type

```lean
theorem typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_positiveDensity (A : BayesianSingleItemAuction I) (hdens : A.HasPositiveDensityOnSupport) (i : I) (hAC : AbsolutelyContinuousOnInterval (A.typeData.cdf i).cdf 0 (A.typeData.omega i)) : IsProbabilityMeasure (A.typeMeasure i)
```

## Dependencies

- HasPositiveDensityOnSupport
- typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_density_nonnegative_ae
- typeDensity_nonnegative_ae_of_hasPositiveDensityOnSupport
