---
id: HasPositiveDensityOnSupport-nonzero-on-support
title: HasPositiveDensityOnSupport.nonzero_on_support
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - HasPositiveDensityOnSupport.nonzero_on_support
uses:
  - HasPositiveDensityOnSupport
  - typeDensity_pos_of_hasPositiveDensityOnSupport
---

# HasPositiveDensityOnSupport.nonzero_on_support

## Lean type

```lean
theorem HasPositiveDensityOnSupport.nonzero_on_support (A : BayesianSingleItemAuction I) (hA : A.HasPositiveDensityOnSupport) {i : I} {v : ℝ} (h0 : 0 < v) (homega : v < A.typeData.omega i) : A.typeDensity i v ≠ 0
```

## Dependencies

- HasPositiveDensityOnSupport
- typeDensity_pos_of_hasPositiveDensityOnSupport
