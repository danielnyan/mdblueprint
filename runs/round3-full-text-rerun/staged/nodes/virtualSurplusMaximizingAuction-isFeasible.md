---
id: virtualSurplusMaximizingAuction-isFeasible
title: virtualSurplusMaximizingAuction_isFeasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isFeasible
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - virtualSurplusMaximizingMechanism_isAllocFeasible
  - virtualSurplusMaximizingAllocationRule_respectsSingleItemCapacity
---

# virtualSurplusMaximizingAuction_isFeasible

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isFeasible [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) : (A.virtualSurplusMaximizingAuction).IsFeasible
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- virtualSurplusMaximizingMechanism_isAllocFeasible
- virtualSurplusMaximizingAllocationRule_respectsSingleItemCapacity
