---
id: virtualSurplusMaximizingMechanism-isDSIC-of-isRegular
title: virtualSurplusMaximizingMechanism_isDSIC_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingMechanism_isDSIC_of_isRegular
uses:
  - IsRegular
  - IsDSIC
  - isDSIC
  - withMyersonPayment_isDSIC_of_isMonotone
  - virtualSurplusMaximizingAllocationRule_isMonotone_of_isRegular
---

# virtualSurplusMaximizingMechanism_isDSIC_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingMechanism_isDSIC_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : (A.virtualSurplusMaximizingMechanism).IsDSIC
```

## Dependencies

- IsRegular
- IsDSIC
- isDSIC
- withMyersonPayment_isDSIC_of_isMonotone
- virtualSurplusMaximizingAllocationRule_isMonotone_of_isRegular
