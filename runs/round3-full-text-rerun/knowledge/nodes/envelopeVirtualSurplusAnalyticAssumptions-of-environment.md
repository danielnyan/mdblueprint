---
id: envelopeVirtualSurplusAnalyticAssumptions-of-environment
title: envelopeVirtualSurplusAnalyticAssumptions_of_environment
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - envelopeVirtualSurplusAnalyticAssumptions_of_environment
uses:
---

# envelopeVirtualSurplusAnalyticAssumptions_of_environment

## Lean type

```lean
theorem envelopeVirtualSurplusAnalyticAssumptions_of_environment {A B : BayesianSingleItemAuction I} (henv : A.EnvelopeVirtualSurplusEnvironmentAssumptions) (hQ : ∀ i : I, IntervalIntegrable (B.interimAllocProb i) volume 0 (A.typeData.omega i)) (hQsurv : ∀ i : I, IntervalIntegrable (fun v => B.interimAllocProb i v * (1 - (A.typeData.cdf i).cdf v)) volume 0 (A.typeData.omega i)) (hvirt : ∀ i : I, IntervalIntegrable (fun v => B.interimAllocProb i v * A.virtualValue i v * A.typeDensity i v) volume 0 (A.typeData.omega i)) : A.EnvelopeVirtualSurplusAnalyticAssumptions B
```

## Dependencies

- none
