---
id: EnvelopeVirtualSurplusAnalyticAssumptions-accumulatedAllocation-density-integrable
title: EnvelopeVirtualSurplusAnalyticAssumptions.accumulatedAllocation_density_integrable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - EnvelopeVirtualSurplusAnalyticAssumptions.accumulatedAllocation_density_integrable
uses:
  - EnvelopeVirtualSurplusAnalyticAssumptions.interim_allocation_intervalIntegrableOnSupport
---

# EnvelopeVirtualSurplusAnalyticAssumptions.accumulatedAllocation_density_integrable

## Lean type

```lean
theorem EnvelopeVirtualSurplusAnalyticAssumptions.accumulatedAllocation_density_integrable {A B : BayesianSingleItemAuction I} (h : A.EnvelopeVirtualSurplusAnalyticAssumptions B) (i : I) : IntervalIntegrable (fun v => (∫ z in 0..v, B.interimAllocProb i z) * A.typeDensity i v) volume 0 (A.typeData.omega i)
```

## Dependencies

- EnvelopeVirtualSurplusAnalyticAssumptions.interim_allocation_intervalIntegrableOnSupport
