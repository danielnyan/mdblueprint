---
id: productPrior-map-eval
title: productPrior_map_eval
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - productPrior_map_eval
uses:
---

# productPrior_map_eval

## Lean type

```lean
theorem productPrior_map_eval [Fintype I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (i : I) : A.productPrior.map (Function.eval i) = A.typeMeasure i
```

## Dependencies

- none
