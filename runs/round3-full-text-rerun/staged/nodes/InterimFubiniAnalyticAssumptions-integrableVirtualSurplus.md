---
id: InterimFubiniAnalyticAssumptions-integrableVirtualSurplus
title: InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
uses:
  - IntegrableVirtualSurplus
---

# InterimFubiniAnalyticAssumptions.integrableVirtualSurplus

## Lean type

```lean
theorem InterimFubiniAnalyticAssumptions.integrableVirtualSurplus [Fintype I] {A B : BayesianSingleItemAuction I} (h : A.InterimFubiniAnalyticAssumptions B) : A.IntegrableVirtualSurplus B.allocationRule
```

## Dependencies

- IntegrableVirtualSurplus
