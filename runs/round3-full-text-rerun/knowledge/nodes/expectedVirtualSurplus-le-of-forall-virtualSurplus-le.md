---
id: expectedVirtualSurplus-le-of-forall-virtualSurplus-le
title: expectedVirtualSurplus_le_of_forall_virtualSurplus_le
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - expectedVirtualSurplus_le_of_forall_virtualSurplus_le
uses:
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
---

# expectedVirtualSurplus_le_of_forall_virtualSurplus_le

## Lean type

```lean
theorem expectedVirtualSurplus_le_of_forall_virtualSurplus_le [Fintype I] (A : BayesianSingleItemAuction I) {x y : (I → ℝ) → I → ℝ} (hx_int : A.IntegrableVirtualSurplus x) (hy_int : A.IntegrableVirtualSurplus y) (hxy : ∀ t, A.virtualSurplus x t ≤ A.virtualSurplus y t) : A.expectedVirtualSurplus x ≤ A.expectedVirtualSurplus y
```

## Dependencies

- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
