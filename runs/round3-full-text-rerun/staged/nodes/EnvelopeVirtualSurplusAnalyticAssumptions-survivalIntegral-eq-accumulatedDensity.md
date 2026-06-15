---
id: EnvelopeVirtualSurplusAnalyticAssumptions-survivalIntegral-eq-accumulatedDensity
title: EnvelopeVirtualSurplusAnalyticAssumptions.survivalIntegral_eq_accumulatedDensity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - EnvelopeVirtualSurplusAnalyticAssumptions.survivalIntegral_eq_accumulatedDensity
uses:
  - survivalIntegral_eq_intervalIntegral_mul_deriv
  - EnvelopeVirtualSurplusAnalyticAssumptions.interim_allocation_intervalIntegrableOnSupport
---

# EnvelopeVirtualSurplusAnalyticAssumptions.survivalIntegral_eq_accumulatedDensity

## Lean type

```lean
theorem EnvelopeVirtualSurplusAnalyticAssumptions.survivalIntegral_eq_accumulatedDensity {A B : BayesianSingleItemAuction I} (h : A.EnvelopeVirtualSurplusAnalyticAssumptions B) (i : I) : (∫ v in 0..A.typeData.omega i, B.interimAllocProb i v * (1 - (A.typeData.cdf i).cdf v)) = ∫ v in 0..A.typeData.omega i, (∫ z in 0..v, B.interimAllocProb i z) * A.typeDensity i v
```

## Dependencies

- survivalIntegral_eq_intervalIntegral_mul_deriv
- EnvelopeVirtualSurplusAnalyticAssumptions.interim_allocation_intervalIntegrableOnSupport
