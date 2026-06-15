---
id: virtualSurplusMaximizingAuction-isDSIC-of-isRegular
title: virtualSurplusMaximizingAuction_isDSIC_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isDSIC_of_isRegular
uses:
  - IsRegular
  - IsDSIC
  - isDSIC
  - virtualSurplusMaximizingMechanism_isDSIC_of_isRegular
---

# virtualSurplusMaximizingAuction_isDSIC_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isDSIC_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : (A.virtualSurplusMaximizingAuction).IsDSIC
```

## Dependencies

- IsRegular
- IsDSIC
- isDSIC
- virtualSurplusMaximizingMechanism_isDSIC_of_isRegular
