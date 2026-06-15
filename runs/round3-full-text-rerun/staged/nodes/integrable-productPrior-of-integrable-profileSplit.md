---
id: integrable-productPrior-of-integrable-profileSplit
title: integrable_productPrior_of_integrable_profileSplit
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integrable_productPrior_of_integrable_profileSplit
uses:
  - OpponentTypeProfile
  - productPrior_map_profileSplitMeasurableEquiv
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# integrable_productPrior_of_integrable_profileSplit

## Lean type

```lean
theorem integrable_productPrior_of_integrable_profileSplit [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (i : I) {E : Type*} [NormedAddCommGroup E] {f : (∀ _ : I, ℝ) → E} (hf : Integrable (fun p : ℝ × OpponentTypeProfile I i => f (reportProfile i p.1 p.2)) ((A.typeMeasure i).prod (A.opponentProductPrior i))) : Integrable f A.productPrior
```

## Dependencies

- OpponentTypeProfile
- productPrior_map_profileSplitMeasurableEquiv
- IsPositiveAffineOf.symm
- Indifferent.symm
