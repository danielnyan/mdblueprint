---
id: typeDensity-measurable
title: typeDensity_measurable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - typeDensity_measurable
uses:
---

# typeDensity_measurable

## Lean type

```lean
theorem typeDensity_measurable (A : BayesianSingleItemAuction I) (i : I) : Measurable (A.typeDensity i)
```

## Dependencies

- none
