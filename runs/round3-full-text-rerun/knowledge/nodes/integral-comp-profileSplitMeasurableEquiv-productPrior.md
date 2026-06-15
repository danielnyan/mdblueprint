---
id: integral-comp-profileSplitMeasurableEquiv-productPrior
title: integral_comp_profileSplitMeasurableEquiv_productPrior
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integral_comp_profileSplitMeasurableEquiv_productPrior
uses:
  - OpponentTypeProfile
  - measurePreserving_profileSplitMeasurableEquiv_productPrior
---

# integral_comp_profileSplitMeasurableEquiv_productPrior

## Lean type

```lean
theorem integral_comp_profileSplitMeasurableEquiv_productPrior [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (i : I) {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] (g : ℝ × OpponentTypeProfile I i → E) : (∫ t, g (profileSplitMeasurableEquiv i t) ∂A.productPrior) = ∫ p, g p ∂(A.typeMeasure i).prod (A.opponentProductPrior i)
```

## Dependencies

- OpponentTypeProfile
- measurePreserving_profileSplitMeasurableEquiv_productPrior
