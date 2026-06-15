---
id: intervalIntegrable-interimExpectedPayment-mul-typeDensity-of-profileSplit-integrable
title: intervalIntegrable_interimExpectedPayment_mul_typeDensity_of_profileSplit_integrable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - intervalIntegrable_interimExpectedPayment_mul_typeDensity_of_profileSplit_integrable
uses:
  - OpponentTypeProfile
---

# intervalIntegrable_interimExpectedPayment_mul_typeDensity_of_profileSplit_integrable

## Lean type

```lean
theorem intervalIntegrable_interimExpectedPayment_mul_typeDensity_of_profileSplit_integrable {A B : BayesianSingleItemAuction I} (i : I) (hmeas : AEMeasurable (fun v => ENNReal.ofReal (A.typeDensity i v)) (volume.restrict (Set.Ioc 0 (A.typeData.omega i)))) (hnonneg : ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) (hpay : Integrable (fun p : ℝ × OpponentTypeProfile I i => B.paymentRule (reportProfile i p.1 p.2) i) ((A.typeMeasure i).prod (B.opponentPrior i))) : IntervalIntegrable (fun v => B.interimExpectedPayment i v * A.typeDensity i v) volume 0 (A.typeData.omega i)
```

## Dependencies

- OpponentTypeProfile
