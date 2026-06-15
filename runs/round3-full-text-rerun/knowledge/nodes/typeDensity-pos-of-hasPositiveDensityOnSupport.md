---
id: typeDensity-pos-of-hasPositiveDensityOnSupport
title: typeDensity_pos_of_hasPositiveDensityOnSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - typeDensity_pos_of_hasPositiveDensityOnSupport
uses:
  - HasPositiveDensityOnSupport
---

# typeDensity_pos_of_hasPositiveDensityOnSupport

## Lean type

```lean
theorem typeDensity_pos_of_hasPositiveDensityOnSupport (A : BayesianSingleItemAuction I) (hA : A.HasPositiveDensityOnSupport) {i : I} {v : ℝ} (h0 : 0 < v) (homega : v < A.typeData.omega i) : 0 < A.typeDensity i v
```

## Dependencies

- HasPositiveDensityOnSupport
