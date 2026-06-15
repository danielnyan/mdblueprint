---
id: expectedVirtualSurplus-le-virtualSurplusMaximizingAllocationRule
title: expectedVirtualSurplus_le_virtualSurplusMaximizingAllocationRule
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - expectedVirtualSurplus_le_virtualSurplusMaximizingAllocationRule
uses:
  - IsFeasible.isSingleItemAllocationRule
  - IsSingleItemAllocationRule
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - expectedVirtualSurplus_le_of_forall_virtualSurplus_le
  - virtualSurplus_le_virtualSurplusMaximizingAllocationRule
---

# expectedVirtualSurplus_le_virtualSurplusMaximizingAllocationRule

## Lean type

```lean
theorem expectedVirtualSurplus_le_virtualSurplusMaximizingAllocationRule [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {x : (I → ℝ) → I → ℝ} (hx : IsSingleItemAllocationRule x) (hx_int : A.IntegrableVirtualSurplus x) (hopt_int : A.IntegrableVirtualSurplus A.virtualSurplusMaximizingAllocationRule) : A.expectedVirtualSurplus x ≤ A.expectedVirtualSurplus A.virtualSurplusMaximizingAllocationRule
```

## Dependencies

- IsFeasible.isSingleItemAllocationRule
- IsSingleItemAllocationRule
- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- expectedVirtualSurplus_le_of_forall_virtualSurplus_le
- virtualSurplus_le_virtualSurplusMaximizingAllocationRule
