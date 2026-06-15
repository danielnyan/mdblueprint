---
id: typeDensity-pos-of-hasPositiveDensityOnSupport-of-profileInterior
title: typeDensity_pos_of_hasPositiveDensityOnSupport_of_profileInterior
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - typeDensity_pos_of_hasPositiveDensityOnSupport_of_profileInterior
uses:
  - HasPositiveDensityOnSupport
  - IsOnTypeProfileInterior
  - typeDensity_pos_of_hasPositiveDensityOnSupport
---

# typeDensity_pos_of_hasPositiveDensityOnSupport_of_profileInterior

## Lean type

```lean
theorem typeDensity_pos_of_hasPositiveDensityOnSupport_of_profileInterior (A : BayesianSingleItemAuction I) (hA : A.HasPositiveDensityOnSupport) {t : I → ℝ} (ht : A.IsOnTypeProfileInterior t) (i : I) : 0 < A.typeDensity i (t i)
```

## Dependencies

- HasPositiveDensityOnSupport
- IsOnTypeProfileInterior
- typeDensity_pos_of_hasPositiveDensityOnSupport
