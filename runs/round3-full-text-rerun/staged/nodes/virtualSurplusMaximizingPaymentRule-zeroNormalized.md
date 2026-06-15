---
id: virtualSurplusMaximizingPaymentRule-zeroNormalized
title: virtualSurplusMaximizingPaymentRule_zeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingPaymentRule_zeroNormalized
uses:
  - ZeroNormalized
  - myersonPayment_zeroNormalized
---

# virtualSurplusMaximizingPaymentRule_zeroNormalized

## Lean type

```lean
theorem virtualSurplusMaximizingPaymentRule_zeroNormalized [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) : SingleParameterMechanism.ZeroNormalized A.virtualSurplusMaximizingPaymentRule
```

## Dependencies

- ZeroNormalized
- myersonPayment_zeroNormalized
