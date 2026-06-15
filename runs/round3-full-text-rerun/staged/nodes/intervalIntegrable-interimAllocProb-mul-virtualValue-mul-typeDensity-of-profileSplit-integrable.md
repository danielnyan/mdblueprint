---
id: intervalIntegrable-interimAllocProb-mul-virtualValue-mul-typeDensity-of-profileSplit-integrable
title: intervalIntegrable_interimAllocProb_mul_virtualValue_mul_typeDensity_of_profileSplit_integrable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - intervalIntegrable_interimAllocProb_mul_virtualValue_mul_typeDensity_of_profileSplit_integrable
uses:
  - OpponentTypeProfile
  - HasSameSellingEnvironment
---

# intervalIntegrable_interimAllocProb_mul_virtualValue_mul_typeDensity_of_profileSplit_integrable

## Lean type

```lean
theorem intervalIntegrable_interimAllocProb_mul_virtualValue_mul_typeDensity_of_profileSplit_integrable {A B : BayesianSingleItemAuction I} (i : I) (hmeas : AEMeasurable (fun v => ENNReal.ofReal (A.typeDensity i v)) (volume.restrict (Set.Ioc 0 (A.typeData.omega i)))) (hnonneg : ∀ᵐ v ∂(volume.restrict (Set.Ioc 0 (A.typeData.omega i))), 0 ≤ A.typeDensity i v) (hvs : Integrable (fun p : ℝ × OpponentTypeProfile I i => B.allocationRule (reportProfile i p.1 p.2) i * A.virtualValue i p.1) ((A.typeMeasure i).prod (B.opponentPrior i))) : IntervalIntegrable (fun v => B.interimAllocProb i v * A.virtualValue i v * A.typeDensity i v) volume 0 (A.typeData.omega i)
```

## Dependencies

- OpponentTypeProfile
- HasSameSellingEnvironment
