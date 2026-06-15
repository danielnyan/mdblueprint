---
id: prior-map-profileSplitMeasurableEquiv-of-hasIndependentTypePriors
title: prior_map_profileSplitMeasurableEquiv_of_hasIndependentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - prior_map_profileSplitMeasurableEquiv_of_hasIndependentTypePriors
uses:
  - HasIndependentTypePriors
  - productPrior_map_profileSplitMeasurableEquiv
---

# prior_map_profileSplitMeasurableEquiv_of_hasIndependentTypePriors

## Lean type

```lean
theorem prior_map_profileSplitMeasurableEquiv_of_hasIndependentTypePriors [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (h : A.HasIndependentTypePriors) (i : I) : A.prior.map (profileSplitMeasurableEquiv i) = (A.typeMeasure i).prod (A.opponentProductPrior i)
```

## Dependencies

- HasIndependentTypePriors
- productPrior_map_profileSplitMeasurableEquiv
