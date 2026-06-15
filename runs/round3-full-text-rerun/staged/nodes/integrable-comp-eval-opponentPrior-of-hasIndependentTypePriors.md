---
id: integrable-comp-eval-opponentPrior-of-hasIndependentTypePriors
title: integrable_comp_eval_opponentPrior_of_hasIndependentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integrable_comp_eval_opponentPrior_of_hasIndependentTypePriors
uses:
  - HasIndependentTypePriors
  - OpponentTypeProfile
  - integrable_comp_eval_opponentProductPrior
---

# integrable_comp_eval_opponentPrior_of_hasIndependentTypePriors

## Lean type

```lean
theorem integrable_comp_eval_opponentPrior_of_hasIndependentTypePriors [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (h : A.HasIndependentTypePriors) {i : I} {j : {j // j ≠ i}} {E : Type*} [NormedAddCommGroup E] {f : ℝ → E} (hf : Integrable f (A.typeMeasure j)) : Integrable (fun t : OpponentTypeProfile I i => f (t j)) (A.opponentPrior i)
```

## Dependencies

- HasIndependentTypePriors
- OpponentTypeProfile
- integrable_comp_eval_opponentProductPrior
