---
id: jointDensity-pos-of-hasPositiveDensityOnSupport-of-profileInterior
title: jointDensity_pos_of_hasPositiveDensityOnSupport_of_profileInterior
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - jointDensity_pos_of_hasPositiveDensityOnSupport_of_profileInterior
uses:
  - HasPositiveDensityOnSupport
  - IsOnTypeProfileInterior
  - HasPositiveJointDensityAt
  - typeDensity_pos_of_hasPositiveDensityOnSupport_of_profileInterior
---

# jointDensity_pos_of_hasPositiveDensityOnSupport_of_profileInterior

## Lean type

```lean
theorem jointDensity_pos_of_hasPositiveDensityOnSupport_of_profileInterior [Fintype I] (A : BayesianSingleItemAuction I) (hA : A.HasPositiveDensityOnSupport) {t : I → ℝ} (ht : A.IsOnTypeProfileInterior t) : A.HasPositiveJointDensityAt t
```

## Dependencies

- HasPositiveDensityOnSupport
- IsOnTypeProfileInterior
- HasPositiveJointDensityAt
- typeDensity_pos_of_hasPositiveDensityOnSupport_of_profileInterior
