---
id: integral-productPrior-eq-integral-typeMeasure-opponentProductPrior
title: integral_productPrior_eq_integral_typeMeasure_opponentProductPrior
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integral_productPrior_eq_integral_typeMeasure_opponentProductPrior
uses:
  - OpponentTypeProfile
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - integral_comp_profileSplitMeasurableEquiv_productPrior
---

# integral_productPrior_eq_integral_typeMeasure_opponentProductPrior

## Lean type

```lean
theorem integral_productPrior_eq_integral_typeMeasure_opponentProductPrior [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (i : I) {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] (f : (∀ _ : I, ℝ) → E) (hf : Integrable (fun p : ℝ × OpponentTypeProfile I i => f (reportProfile i p.1 p.2)) ((A.typeMeasure i).prod (A.opponentProductPrior i))) : (∫ t, f t ∂A.productPrior) = ∫ v, ∫ t, f (reportProfile i v t) ∂A.opponentProductPrior i ∂A.typeMeasure i
```

## Dependencies

- OpponentTypeProfile
- IsPositiveAffineOf.symm
- Indifferent.symm
- integral_comp_profileSplitMeasurableEquiv_productPrior
