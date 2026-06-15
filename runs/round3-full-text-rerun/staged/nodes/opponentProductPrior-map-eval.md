---
id: opponentProductPrior-map-eval
title: opponentProductPrior_map_eval
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - opponentProductPrior_map_eval
uses:
---

# opponentProductPrior_map_eval

## Lean type

```lean
theorem opponentProductPrior_map_eval [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (i : I) (j : {j // j ≠ i}) : (A.opponentProductPrior i).map (Function.eval j) = A.typeMeasure j
```

## Dependencies

- none
