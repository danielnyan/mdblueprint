---
id: integral-comp-eval-opponentPrior-of-hasIndependentTypePriors
title: integral_comp_eval_opponentPrior_of_hasIndependentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integral_comp_eval_opponentPrior_of_hasIndependentTypePriors
uses:
  - HasIndependentTypePriors
  - OpponentTypeProfile
  - integral_comp_eval_opponentProductPrior
---

# integral_comp_eval_opponentPrior_of_hasIndependentTypePriors

## Lean type

```lean
theorem integral_comp_eval_opponentPrior_of_hasIndependentTypePriors [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (h : A.HasIndependentTypePriors) {i : I} {j : {j // j ≠ i}} {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] {f : ℝ → E} (hf : AEStronglyMeasurable f (A.typeMeasure j)) : (∫ t : OpponentTypeProfile I i, f (t j) ∂A.opponentPrior i) = ∫ v, f v ∂A.typeMeasure j
```

## Dependencies

- HasIndependentTypePriors
- OpponentTypeProfile
- integral_comp_eval_opponentProductPrior
