---
id: RegularMyersonICIRAnalyticAssumptions-typeDensity-nonnegative-ae
title: RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
uses:
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
---

# RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae

## Lean type

```lean
theorem RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] {A : BayesianSingleItemAuction I} (h : A.RegularMyersonICIRAnalyticAssumptions) (i : I) : ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v
```

## Dependencies

- EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
