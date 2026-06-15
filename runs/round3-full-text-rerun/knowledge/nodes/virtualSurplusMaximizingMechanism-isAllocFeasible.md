---
id: virtualSurplusMaximizingMechanism-isAllocFeasible
title: virtualSurplusMaximizingMechanism_isAllocFeasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingMechanism_isAllocFeasible
uses:
  - IsAllocFeasible
  - withPayment_isAllocFeasible_of_isSingleItemAllocationRule
  - virtualSurplusMaximizingAllocationRule_isSingleItemAllocationRule
---

# virtualSurplusMaximizingMechanism_isAllocFeasible

## Lean type

```lean
theorem virtualSurplusMaximizingMechanism_isAllocFeasible [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) : (A.virtualSurplusMaximizingMechanism).IsAllocFeasible
```

## Dependencies

- IsAllocFeasible
- withPayment_isAllocFeasible_of_isSingleItemAllocationRule
- virtualSurplusMaximizingAllocationRule_isSingleItemAllocationRule
