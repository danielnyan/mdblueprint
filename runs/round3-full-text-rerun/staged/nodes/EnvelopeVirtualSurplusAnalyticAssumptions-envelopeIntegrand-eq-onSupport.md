---
id: EnvelopeVirtualSurplusAnalyticAssumptions-envelopeIntegrand-eq-onSupport
title: EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegrand_eq_onSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegrand_eq_onSupport
uses:
  - HasPositiveDensityOnSupport.nonzero_on_support
---

# EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegrand_eq_onSupport

## Lean type

```lean
theorem EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegrand_eq_onSupport {A B : BayesianSingleItemAuction I} (h : A.EnvelopeVirtualSurplusAnalyticAssumptions B) (i : I) : Set.EqOn (fun v => (B.interimAllocProb i v * v - ∫ z in 0..v, B.interimAllocProb i z) * A.typeDensity i v) (fun v => B.interimAllocProb i v * A.virtualValue i v * A.typeDensity i v + B.interimAllocProb i v * (1 - (A.typeData.cdf i).cdf v) - (∫ z in 0..v, B.interimAllocProb i z) * A.typeDensity i v) (Set.uIoc 0 (A.typeData.omega i))
```

## Dependencies

- HasPositiveDensityOnSupport.nonzero_on_support
