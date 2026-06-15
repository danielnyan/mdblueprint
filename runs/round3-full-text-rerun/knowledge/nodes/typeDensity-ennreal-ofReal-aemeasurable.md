---
id: typeDensity-ennreal-ofReal-aemeasurable
title: typeDensity_ennreal_ofReal_aemeasurable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - typeDensity_ennreal_ofReal_aemeasurable
uses:
  - typeDensity_measurable
---

# typeDensity_ennreal_ofReal_aemeasurable

## Lean type

```lean
theorem typeDensity_ennreal_ofReal_aemeasurable (A : BayesianSingleItemAuction I) (i : I) : AEMeasurable (fun v => ENNReal.ofReal (A.typeDensity i v)) (volume.restrict (Set.Ioc 0 (A.typeData.omega i)))
```

## Dependencies

- typeDensity_measurable
