---
id: EnvelopeVirtualSurplusAnalyticAssumptions-interim-allocation-intervalIntegrableOnSupport
title: EnvelopeVirtualSurplusAnalyticAssumptions.interim_allocation_intervalIntegrableOnSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - EnvelopeVirtualSurplusAnalyticAssumptions.interim_allocation_intervalIntegrableOnSupport
uses:
---

# EnvelopeVirtualSurplusAnalyticAssumptions.interim_allocation_intervalIntegrableOnSupport

## Lean type

```lean
theorem EnvelopeVirtualSurplusAnalyticAssumptions.interim_allocation_intervalIntegrableOnSupport {A B : BayesianSingleItemAuction I} (h : A.EnvelopeVirtualSurplusAnalyticAssumptions B) (i : I) : IntervalIntegrable (B.interimAllocProb i) volume 0 (A.typeData.omega i)
```

## Dependencies

- none
