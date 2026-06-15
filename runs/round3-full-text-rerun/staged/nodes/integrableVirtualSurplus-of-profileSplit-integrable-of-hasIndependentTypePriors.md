---
id: integrableVirtualSurplus-of-profileSplit-integrable-of-hasIndependentTypePriors
title: integrableVirtualSurplus_of_profileSplit_integrable_of_hasIndependentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - integrableVirtualSurplus_of_profileSplit_integrable_of_hasIndependentTypePriors
uses:
  - HasIndependentTypePriors
  - HasSameSellingEnvironment
  - OpponentTypeProfile
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - integrable_prior_of_integrable_profileSplit_of_hasIndependentTypePriors
  - HasSameSellingEnvironment.opponentPrior_eq
---

# integrableVirtualSurplus_of_profileSplit_integrable_of_hasIndependentTypePriors

## Lean type

```lean
theorem integrableVirtualSurplus_of_profileSplit_integrable_of_hasIndependentTypePriors [Fintype I] [DecidableEq I] {A B : BayesianSingleItemAuction I} [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (hind : A.HasIndependentTypePriors) (henv : A.HasSameSellingEnvironment B) (hvs_prod_int : ∀ i : I, Integrable (fun p : ℝ × OpponentTypeProfile I i => B.allocationRule (reportProfile i p.1 p.2) i * A.virtualValue i p.1) ((A.typeMeasure i).prod (B.opponentPrior i))) : A.IntegrableVirtualSurplus B.allocationRule
```

## Dependencies

- HasIndependentTypePriors
- HasSameSellingEnvironment
- OpponentTypeProfile
- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- integrable_prior_of_integrable_profileSplit_of_hasIndependentTypePriors
- HasSameSellingEnvironment.opponentPrior_eq
