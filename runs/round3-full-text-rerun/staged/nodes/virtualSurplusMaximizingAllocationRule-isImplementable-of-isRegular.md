---
id: virtualSurplusMaximizingAllocationRule-isImplementable-of-isRegular
title: virtualSurplusMaximizingAllocationRule_isImplementable_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_isImplementable_of_isRegular
uses:
  - IsRegular
  - IsImplementable
  - isImplementable_of_isMonotone
  - virtualSurplusMaximizingAllocationRule_isMonotone_of_isRegular
---

# virtualSurplusMaximizingAllocationRule_isImplementable_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_isImplementable_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : SingleParameterMechanism.IsImplementable A.virtualSurplusMaximizingAllocationRule
```

## Dependencies

- IsRegular
- IsImplementable
- isImplementable_of_isMonotone
- virtualSurplusMaximizingAllocationRule_isMonotone_of_isRegular
