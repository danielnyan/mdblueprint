---
id: integrable-comp-eval-productPrior
title: integrable_comp_eval_productPrior
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integrable_comp_eval_productPrior
uses:
---

# integrable_comp_eval_productPrior

## Lean type

```lean
theorem integrable_comp_eval_productPrior [Fintype I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] {i : I} {E : Type*} [NormedAddCommGroup E] {f : ℝ → E} (hf : Integrable f (A.typeMeasure i)) : Integrable (fun t : ∀ _ : I, ℝ => f (t i)) A.productPrior
```

## Dependencies

- none
