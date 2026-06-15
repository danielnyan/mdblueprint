---
id: paymentInterimFubiniAssumptions-of-independentTypePriors
title: paymentInterimFubiniAssumptions_of_independentTypePriors
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - paymentInterimFubiniAssumptions_of_independentTypePriors
uses:
  - HasIndependentTypePriors
  - HasSameSellingEnvironment
  - OpponentTypeProfile
  - paymentInterimFubiniAssumptions_of_typeMeasure_fubini
  - integrable_prior_of_integrable_profileSplit_of_hasIndependentTypePriors
  - HasSameSellingEnvironment.opponentPrior_eq
  - integral_prior_eq_integral_typeMeasure_opponentPrior_of_hasIndependentTypePriors
---

# paymentInterimFubiniAssumptions_of_independentTypePriors

## Lean type

```lean
theorem paymentInterimFubiniAssumptions_of_independentTypePriors [Fintype I] [DecidableEq I] {A B : BayesianSingleItemAuction I} [∀ i : I, IsProbabilityMeasure (A.typeMeasure i)] (hdens_meas : ∀ i : I, AEMeasurable (fun v => ENNReal.ofReal (A.typeDensity i v)) (volume.restrict (Set.Ioc 0 (A.typeData.omega i)))) (hdens_ae : ∀ i : I, ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) (hind : A.HasIndependentTypePriors) (henv : A.HasSameSellingEnvironment B) (hpay_prod_int : ∀ i : I, Integrable (fun p : ℝ × OpponentTypeProfile I i => B.paymentRule (reportProfile i p.1 p.2) i) ((A.typeMeasure i).prod (B.opponentPrior i))) : A.PaymentInterimFubiniAssumptions B
```

## Dependencies

- HasIndependentTypePriors
- HasSameSellingEnvironment
- OpponentTypeProfile
- paymentInterimFubiniAssumptions_of_typeMeasure_fubini
- integrable_prior_of_integrable_profileSplit_of_hasIndependentTypePriors
- HasSameSellingEnvironment.opponentPrior_eq
- integral_prior_eq_integral_typeMeasure_opponentPrior_of_hasIndependentTypePriors
