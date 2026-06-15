---
id: productPrior-map-profileSplitMeasurableEquiv
title: productPrior_map_profileSplitMeasurableEquiv
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - productPrior_map_profileSplitMeasurableEquiv
uses:
  - measurePreserving_profileSplitMeasurableEquiv_productPrior
---

# productPrior_map_profileSplitMeasurableEquiv

## Lean type

```lean
theorem productPrior_map_profileSplitMeasurableEquiv [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (i : I) : A.productPrior.map (profileSplitMeasurableEquiv i) = (A.typeMeasure i).prod (A.opponentProductPrior i)
```

## Dependencies

- measurePreserving_profileSplitMeasurableEquiv_productPrior
