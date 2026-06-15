---
id: prior-map-eval-of-hasIndependentTypePriors
title: prior_map_eval_of_hasIndependentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - prior_map_eval_of_hasIndependentTypePriors
uses:
  - HasIndependentTypePriors
  - productPrior_map_eval
---

# prior_map_eval_of_hasIndependentTypePriors

## Lean type

```lean
theorem prior_map_eval_of_hasIndependentTypePriors [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (h : A.HasIndependentTypePriors) (i : I) : A.prior.map (Function.eval i) = A.typeMeasure i
```

## Dependencies

- HasIndependentTypePriors
- productPrior_map_eval
