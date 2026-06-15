---
id: integral-comp-eval-prior-of-hasIndependentTypePriors
title: integral_comp_eval_prior_of_hasIndependentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integral_comp_eval_prior_of_hasIndependentTypePriors
uses:
  - HasIndependentTypePriors
  - integral_comp_eval_productPrior
---

# integral_comp_eval_prior_of_hasIndependentTypePriors

## Lean type

```lean
theorem integral_comp_eval_prior_of_hasIndependentTypePriors [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (h : A.HasIndependentTypePriors) {i : I} {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] {f : ℝ → E} (hf : AEStronglyMeasurable f (A.typeMeasure i)) : (∫ t : ∀ _ : I, ℝ, f (t i) ∂A.prior) = ∫ v, f v ∂A.typeMeasure i
```

## Dependencies

- HasIndependentTypePriors
- integral_comp_eval_productPrior
