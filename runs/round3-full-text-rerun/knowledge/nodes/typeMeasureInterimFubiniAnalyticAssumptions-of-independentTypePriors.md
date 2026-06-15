---
id: typeMeasureInterimFubiniAnalyticAssumptions-of-independentTypePriors
title: typeMeasureInterimFubiniAnalyticAssumptions_of_independentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - typeMeasureInterimFubiniAnalyticAssumptions_of_independentTypePriors
uses:
  - HasIndependentTypePriors
  - HasSameSellingEnvironment
  - OpponentTypeProfile
  - integrable_prior_of_integrable_profileSplit_of_hasIndependentTypePriors
  - HasSameSellingEnvironment.opponentPrior_eq
  - typeDensity_measurable
  - typeDensity_ennreal_ofReal_aemeasurable
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
  - RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
  - integral_prior_eq_integral_typeMeasure_opponentPrior_of_hasIndependentTypePriors
---

# typeMeasureInterimFubiniAnalyticAssumptions_of_independentTypePriors

## Lean type

```lean
theorem typeMeasureInterimFubiniAnalyticAssumptions_of_independentTypePriors [Fintype I] [DecidableEq I] {A B : BayesianSingleItemAuction I} [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (hdens_ae : ∀ i : I, ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) (hind : A.HasIndependentTypePriors) (henv : A.HasSameSellingEnvironment B) (hpay_prod_int : ∀ i : I, Integrable (fun p : ℝ × OpponentTypeProfile I i => B.paymentRule (reportProfile i p.1 p.2) i) ((A.typeMeasure i).prod (B.opponentPrior i))) (hvs_prod_int : ∀ i : I, Integrable (fun p : ℝ × OpponentTypeProfile I i => B.allocationRule (reportProfile i p.1 p.2) i * A.virtualValue i p.1) ((A.typeMeasure i).prod (B.opponentPrior i))) : A.TypeMeasureInterimFubiniAnalyticAssumptions B
```

## Dependencies

- HasIndependentTypePriors
- HasSameSellingEnvironment
- OpponentTypeProfile
- integrable_prior_of_integrable_profileSplit_of_hasIndependentTypePriors
- HasSameSellingEnvironment.opponentPrior_eq
- typeDensity_measurable
- typeDensity_ennreal_ofReal_aemeasurable
- EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
- RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
- integral_prior_eq_integral_typeMeasure_opponentPrior_of_hasIndependentTypePriors
