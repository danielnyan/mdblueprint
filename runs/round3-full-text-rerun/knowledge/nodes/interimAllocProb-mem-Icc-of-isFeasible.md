---
id: interimAllocProb-mem-Icc-of-isFeasible
title: interimAllocProb_mem_Icc_of_isFeasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimAllocProb_mem_Icc_of_isFeasible
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - HasIntegrableInterimAllocation
  - interimAllocProb_nonneg_of_isFeasible
  - interimAllocProb_le_one_of_isFeasible
---

# interimAllocProb_mem_Icc_of_isFeasible

## Lean type

```lean
theorem interimAllocProb_mem_Icc_of_isFeasible [Fintype I] (A : BayesianSingleItemAuction I) (hfeas : A.IsFeasible) (hint : A.HasIntegrableInterimAllocation) (i : I) (z_i : ℝ) : A.interimAllocProb i z_i ∈ Set.Icc (0 : ℝ) 1
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- HasIntegrableInterimAllocation
- interimAllocProb_nonneg_of_isFeasible
- interimAllocProb_le_one_of_isFeasible
