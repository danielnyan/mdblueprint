---
id: expectedVirtualSurplus-le-virtualSurplusMaximizingAuction-of-isFeasible
title: expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_of_isFeasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_of_isFeasible
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_allocationRule
  - IsFeasible.isSingleItemAllocationRule
  - IsSingleItemAllocationRule
---

# expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_of_isFeasible

## Lean type

```lean
theorem expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_of_isFeasible [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A B : BayesianSingleItemAuction I) (hB : B.IsFeasible) (hB_int : A.IntegrableVirtualSurplus B.allocationRule) (hopt_int : A.IntegrableVirtualSurplus (A.virtualSurplusMaximizingAuction).allocationRule) : A.expectedVirtualSurplus B.allocationRule ≤ A.expectedVirtualSurplus (A.virtualSurplusMaximizingAuction).allocationRule
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_allocationRule
- IsFeasible.isSingleItemAllocationRule
- IsSingleItemAllocationRule
