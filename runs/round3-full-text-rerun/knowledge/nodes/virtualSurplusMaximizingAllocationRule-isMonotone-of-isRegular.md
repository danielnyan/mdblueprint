---
id: virtualSurplusMaximizingAllocationRule-isMonotone-of-isRegular
title: virtualSurplusMaximizingAllocationRule_isMonotone_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_isMonotone_of_isRegular
uses:
  - IsRegular
  - IsMonotone
  - virtualSurplusMaximizingAllocationRule_nonneg
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# virtualSurplusMaximizingAllocationRule_isMonotone_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_isMonotone_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : SingleParameterMechanism.IsMonotone ({ allocationRule
```

## Dependencies

- IsRegular
- IsMonotone
- virtualSurplusMaximizingAllocationRule_nonneg
- IsPositiveAffineOf.symm
- Indifferent.symm
