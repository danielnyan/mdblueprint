---
id: typeMeasure-isProbabilityMeasure-of-cdf-absolutelyContinuous-of-density-nonnegative-ae
title: typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_density_nonnegative_ae
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_density_nonnegative_ae
uses:
---

# typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_density_nonnegative_ae

## Lean type

```lean
theorem typeMeasure_isProbabilityMeasure_of_cdf_absolutelyContinuous_of_density_nonnegative_ae (A : BayesianSingleItemAuction I) (i : I) (hAC : AbsolutelyContinuousOnInterval (A.typeData.cdf i).cdf 0 (A.typeData.omega i)) (hdens_ae : ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) : IsProbabilityMeasure (A.typeMeasure i)
```

## Dependencies

- none
