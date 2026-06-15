---
id: virtualSurplusMaximizingAuction-isZeroNormalized
title: virtualSurplusMaximizingAuction_isZeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_isZeroNormalized
uses:
  - IsZeroNormalized
  - virtualSurplusMaximizingPaymentRule_zeroNormalized
---

# virtualSurplusMaximizingAuction_isZeroNormalized

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_isZeroNormalized [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) : (A.virtualSurplusMaximizingAuction).IsZeroNormalized
```

## Dependencies

- IsZeroNormalized
- virtualSurplusMaximizingPaymentRule_zeroNormalized
