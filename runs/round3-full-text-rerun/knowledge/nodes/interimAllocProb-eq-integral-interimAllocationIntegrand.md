---
id: interimAllocProb-eq-integral-interimAllocationIntegrand
title: interimAllocProb_eq_integral_interimAllocationIntegrand
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimAllocProb_eq_integral_interimAllocationIntegrand
uses:
---

# interimAllocProb_eq_integral_interimAllocationIntegrand

## Lean type

```lean
theorem interimAllocProb_eq_integral_interimAllocationIntegrand (A : BayesianSingleItemAuction I) (i : I) (z_i : ℝ) : A.interimAllocProb i z_i = ∫ t, A.interimAllocationIntegrand i z_i t ∂A.opponentPrior i
```

## Dependencies

- none
