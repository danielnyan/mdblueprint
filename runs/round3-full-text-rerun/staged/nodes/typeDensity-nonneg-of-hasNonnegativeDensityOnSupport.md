---
id: typeDensity-nonneg-of-hasNonnegativeDensityOnSupport
title: typeDensity_nonneg_of_hasNonnegativeDensityOnSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - typeDensity_nonneg_of_hasNonnegativeDensityOnSupport
uses:
  - HasNonnegativeDensityOnSupport
---

# typeDensity_nonneg_of_hasNonnegativeDensityOnSupport

## Lean type

```lean
theorem typeDensity_nonneg_of_hasNonnegativeDensityOnSupport (A : BayesianSingleItemAuction I) (hA : A.HasNonnegativeDensityOnSupport) {i : I} {v : ℝ} (h0 : 0 ≤ v) (homega : v ≤ A.typeData.omega i) : 0 ≤ A.typeDensity i v
```

## Dependencies

- HasNonnegativeDensityOnSupport
