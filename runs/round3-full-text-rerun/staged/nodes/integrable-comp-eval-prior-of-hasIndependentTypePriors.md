---
id: integrable-comp-eval-prior-of-hasIndependentTypePriors
title: integrable_comp_eval_prior_of_hasIndependentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integrable_comp_eval_prior_of_hasIndependentTypePriors
uses:
  - HasIndependentTypePriors
  - integrable_comp_eval_productPrior
---

# integrable_comp_eval_prior_of_hasIndependentTypePriors

## Lean type

```lean
theorem integrable_comp_eval_prior_of_hasIndependentTypePriors [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (h : A.HasIndependentTypePriors) {i : I} {E : Type*} [NormedAddCommGroup E] {f : ℝ → E} (hf : Integrable f (A.typeMeasure i)) : Integrable (fun t : ∀ _ : I, ℝ => f (t i)) A.prior
```

## Dependencies

- HasIndependentTypePriors
- integrable_comp_eval_productPrior
