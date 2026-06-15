---
id: EnvelopeVirtualSurplusEnvironmentAssumptions-typeDensity-nonnegative-ae
title: EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
uses:
  - typeDensity_nonnegative_ae_of_hasPositiveDensityOnSupport
---

# EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae

## Lean type

```lean
theorem EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae {A : BayesianSingleItemAuction I} (h : A.EnvelopeVirtualSurplusEnvironmentAssumptions) (i : I) : ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v
```

## Dependencies

- typeDensity_nonnegative_ae_of_hasPositiveDensityOnSupport
