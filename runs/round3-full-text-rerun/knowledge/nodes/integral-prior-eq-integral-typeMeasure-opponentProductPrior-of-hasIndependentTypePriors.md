---
id: integral-prior-eq-integral-typeMeasure-opponentProductPrior-of-hasIndependentTypePriors
title: integral_prior_eq_integral_typeMeasure_opponentProductPrior_of_hasIndependentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integral_prior_eq_integral_typeMeasure_opponentProductPrior_of_hasIndependentTypePriors
uses:
  - HasIndependentTypePriors
  - OpponentTypeProfile
  - integral_productPrior_eq_integral_typeMeasure_opponentProductPrior
---

# integral_prior_eq_integral_typeMeasure_opponentProductPrior_of_hasIndependentTypePriors

## Lean type

```lean
theorem integral_prior_eq_integral_typeMeasure_opponentProductPrior_of_hasIndependentTypePriors [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (h : A.HasIndependentTypePriors) (i : I) {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] (f : (∀ _ : I, ℝ) → E) (hf : Integrable (fun p : ℝ × OpponentTypeProfile I i => f (reportProfile i p.1 p.2)) ((A.typeMeasure i).prod (A.opponentProductPrior i))) : (∫ t, f t ∂A.prior) = ∫ v, ∫ t, f (reportProfile i v t) ∂A.opponentProductPrior i ∂A.typeMeasure i
```

## Dependencies

- HasIndependentTypePriors
- OpponentTypeProfile
- integral_productPrior_eq_integral_typeMeasure_opponentProductPrior
