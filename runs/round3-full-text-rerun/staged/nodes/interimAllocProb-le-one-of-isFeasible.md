---
id: interimAllocProb-le-one-of-isFeasible
title: interimAllocProb_le_one_of_isFeasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimAllocProb_le_one_of_isFeasible
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - HasIntegrableInterimAllocation
  - OpponentTypeProfile
---

# interimAllocProb_le_one_of_isFeasible

## Lean type

```lean
theorem interimAllocProb_le_one_of_isFeasible [Fintype I] (A : BayesianSingleItemAuction I) (hfeas : A.IsFeasible) (hint : A.HasIntegrableInterimAllocation) (i : I) (z_i : ℝ) : A.interimAllocProb i z_i ≤ 1
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- HasIntegrableInterimAllocation
- OpponentTypeProfile
