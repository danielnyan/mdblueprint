---
id: EnvelopeVirtualSurplusAnalyticAssumptions-envelope-density-integrable
title: EnvelopeVirtualSurplusAnalyticAssumptions.envelope_density_integrable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - EnvelopeVirtualSurplusAnalyticAssumptions.envelope_density_integrable
uses:
  - EnvelopeVirtualSurplusAnalyticAssumptions.accumulatedAllocation_density_integrable
  - EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegrand_eq_onSupport
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# EnvelopeVirtualSurplusAnalyticAssumptions.envelope_density_integrable

## Lean type

```lean
theorem EnvelopeVirtualSurplusAnalyticAssumptions.envelope_density_integrable {A B : BayesianSingleItemAuction I} (h : A.EnvelopeVirtualSurplusAnalyticAssumptions B) (i : I) : IntervalIntegrable (fun v => (B.interimAllocProb i v * v - ∫ z in 0..v, B.interimAllocProb i z) * A.typeDensity i v) volume 0 (A.typeData.omega i)
```

## Dependencies

- EnvelopeVirtualSurplusAnalyticAssumptions.accumulatedAllocation_density_integrable
- EnvelopeVirtualSurplusAnalyticAssumptions.envelopeIntegrand_eq_onSupport
- IsPositiveAffineOf.symm
- Indifferent.symm
