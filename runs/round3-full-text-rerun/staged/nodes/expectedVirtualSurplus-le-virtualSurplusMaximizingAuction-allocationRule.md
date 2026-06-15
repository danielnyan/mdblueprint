---
id: expectedVirtualSurplus-le-virtualSurplusMaximizingAuction-allocationRule
title: expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_allocationRule
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_allocationRule
uses:
  - IsFeasible.isSingleItemAllocationRule
  - IsSingleItemAllocationRule
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - expectedVirtualSurplus_le_virtualSurplusMaximizingAllocationRule
---

# expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_allocationRule

## Lean type

```lean
theorem expectedVirtualSurplus_le_virtualSurplusMaximizingAuction_allocationRule [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {x : (I → ℝ) → I → ℝ} (hx : IsSingleItemAllocationRule x) (hx_int : A.IntegrableVirtualSurplus x) (hopt_int : A.IntegrableVirtualSurplus (A.virtualSurplusMaximizingAuction).allocationRule) : A.expectedVirtualSurplus x ≤ A.expectedVirtualSurplus (A.virtualSurplusMaximizingAuction).allocationRule
```

## Dependencies

- IsFeasible.isSingleItemAllocationRule
- IsSingleItemAllocationRule
- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- expectedVirtualSurplus_le_virtualSurplusMaximizingAllocationRule
