---
id: IsVirtualSurplusOptimalAllocationRule
title: IsVirtualSurplusOptimalAllocationRule
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsVirtualSurplusOptimalAllocationRule
uses:
  - IsFeasible.isSingleItemAllocationRule
  - IsSingleItemAllocationRule
---

# IsVirtualSurplusOptimalAllocationRule

## Lean type

```lean
def IsVirtualSurplusOptimalAllocationRule [Fintype I] (A : BayesianSingleItemAuction I) (x : (I → ℝ) → I → ℝ) : Prop
```

## Dependencies

- IsFeasible.isSingleItemAllocationRule
- IsSingleItemAllocationRule
