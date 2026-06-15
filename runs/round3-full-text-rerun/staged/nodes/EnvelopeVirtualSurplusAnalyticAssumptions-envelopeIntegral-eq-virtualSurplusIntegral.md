---
id: EnvelopeVirtualSurplusAnalyticAssumptions-envelopeIntegral-eq-virtualSurplusIntegral
title: EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegral_eq_virtualSurplusIntegral
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegral_eq_virtualSurplusIntegral
uses:
  - EnvelopeVirtualSurplusAnalyticAssumptions.survivalIntegral_eq_accumulatedDensity
  - EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegrand_eq_onSupport
  - EnvelopeVirtualSurplusAnalyticAssumptions.accumulatedAllocation_density_integrable
---

# EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegral_eq_virtualSurplusIntegral

## Lean type

```lean
theorem EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegral_eq_virtualSurplusIntegral {A B : BayesianSingleItemAuction I} (h : A.EnvelopeVirtualSurplusAnalyticAssumptions B) (i : I) : (∫ v in 0..A.typeData.omega i, (B.interimAllocProb i v * v - ∫ z in 0..v, B.interimAllocProb i z) * A.typeDensity i v) = ∫ v in 0..A.typeData.omega i, B.interimAllocProb i v * A.virtualValue i v * A.typeDensity i v
```

## Dependencies

- EnvelopeVirtualSurplusAnalyticAssumptions.survivalIntegral_eq_accumulatedDensity
- EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegrand_eq_onSupport
- EnvelopeVirtualSurplusAnalyticAssumptions.accumulatedAllocation_density_integrable
