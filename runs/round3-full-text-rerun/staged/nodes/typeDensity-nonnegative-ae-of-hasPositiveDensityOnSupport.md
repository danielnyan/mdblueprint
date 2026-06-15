---
id: typeDensity-nonnegative-ae-of-hasPositiveDensityOnSupport
title: typeDensity_nonnegative_ae_of_hasPositiveDensityOnSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - typeDensity_nonnegative_ae_of_hasPositiveDensityOnSupport
uses:
  - HasPositiveDensityOnSupport
  - typeDensity_pos_of_hasPositiveDensityOnSupport
---

# typeDensity_nonnegative_ae_of_hasPositiveDensityOnSupport

## Lean type

```lean
theorem typeDensity_nonnegative_ae_of_hasPositiveDensityOnSupport (A : BayesianSingleItemAuction I) (hA : A.HasPositiveDensityOnSupport) (i : I) : ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v
```

## Dependencies

- HasPositiveDensityOnSupport
- typeDensity_pos_of_hasPositiveDensityOnSupport
