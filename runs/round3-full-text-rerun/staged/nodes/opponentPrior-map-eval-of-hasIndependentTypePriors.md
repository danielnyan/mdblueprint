---
id: opponentPrior-map-eval-of-hasIndependentTypePriors
title: opponentPrior_map_eval_of_hasIndependentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - opponentPrior_map_eval_of_hasIndependentTypePriors
uses:
  - HasIndependentTypePriors
  - opponentProductPrior_map_eval
---

# opponentPrior_map_eval_of_hasIndependentTypePriors

## Lean type

```lean
theorem opponentPrior_map_eval_of_hasIndependentTypePriors [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (h : A.HasIndependentTypePriors) (i : I) (j : {j // j ≠ i}) : (A.opponentPrior i).map (Function.eval j) = A.typeMeasure j
```

## Dependencies

- HasIndependentTypePriors
- opponentProductPrior_map_eval
