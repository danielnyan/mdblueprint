---
id: virtualSurplusMaximizingAllocationRule-isSingleItemAllocationRule
title: virtualSurplusMaximizingAllocationRule_isSingleItemAllocationRule
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_isSingleItemAllocationRule
uses:
  - IsFeasible.isSingleItemAllocationRule
  - IsSingleItemAllocationRule
  - virtualSurplusMaximizingAllocationRule_nonneg
  - virtualSurplusMaximizingAllocationRule_respectsSingleItemCapacity
---

# virtualSurplusMaximizingAllocationRule_isSingleItemAllocationRule

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_isSingleItemAllocationRule [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) : IsSingleItemAllocationRule A.virtualSurplusMaximizingAllocationRule
```

## Dependencies

- IsFeasible.isSingleItemAllocationRule
- IsSingleItemAllocationRule
- virtualSurplusMaximizingAllocationRule_nonneg
- virtualSurplusMaximizingAllocationRule_respectsSingleItemCapacity
