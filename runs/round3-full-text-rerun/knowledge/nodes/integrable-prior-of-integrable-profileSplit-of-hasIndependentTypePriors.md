---
id: integrable-prior-of-integrable-profileSplit-of-hasIndependentTypePriors
title: integrable_prior_of_integrable_profileSplit_of_hasIndependentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integrable_prior_of_integrable_profileSplit_of_hasIndependentTypePriors
uses:
  - HasIndependentTypePriors
  - OpponentTypeProfile
  - integrable_productPrior_of_integrable_profileSplit
---

# integrable_prior_of_integrable_profileSplit_of_hasIndependentTypePriors

## Lean type

```lean
theorem integrable_prior_of_integrable_profileSplit_of_hasIndependentTypePriors [Fintype I] [DecidableEq I] (A : BayesianSingleItemAuction I) [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (h : A.HasIndependentTypePriors) (i : I) {E : Type*} [NormedAddCommGroup E] {f : (∀ _ : I, ℝ) → E} (hf : Integrable (fun p : ℝ × OpponentTypeProfile I i => f (reportProfile i p.1 p.2)) ((A.typeMeasure i).prod (A.opponentPrior i))) : Integrable f A.prior
```

## Dependencies

- HasIndependentTypePriors
- OpponentTypeProfile
- integrable_productPrior_of_integrable_profileSplit
