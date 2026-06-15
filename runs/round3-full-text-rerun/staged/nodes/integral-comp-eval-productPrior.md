---
id: integral-comp-eval-productPrior
title: integral_comp_eval_productPrior
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integral_comp_eval_productPrior
uses:
---

# integral_comp_eval_productPrior

## Lean type

```lean
theorem integral_comp_eval_productPrior [Fintype I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] {i : I} {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] {f : ℝ → E} (hf : AEStronglyMeasurable f (A.typeMeasure i)) : (∫ t : ∀ _ : I, ℝ, f (t i) ∂A.productPrior) = ∫ v, f v ∂A.typeMeasure i
```

## Dependencies

- none
