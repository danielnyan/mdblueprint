---
id: interimAllocProb-nonneg-of-isFeasible
title: interimAllocProb_nonneg_of_isFeasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimAllocProb_nonneg_of_isFeasible
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
---

# interimAllocProb_nonneg_of_isFeasible

## Lean type

```lean
theorem interimAllocProb_nonneg_of_isFeasible [Fintype I] (A : BayesianSingleItemAuction I) (hfeas : A.IsFeasible) (i : I) (z_i : ℝ) : 0 ≤ A.interimAllocProb i z_i
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
