---
id: paymentRule-eq-virtualSurplusMaximizingPaymentRule-of-isDSIC-of-zeroNormalized
title: paymentRule_eq_virtualSurplusMaximizingPaymentRule_of_isDSIC_of_zeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - paymentRule_eq_virtualSurplusMaximizingPaymentRule_of_isDSIC_of_zeroNormalized
uses:
  - IsDSIC
  - isDSIC
  - ZeroNormalized
  - payment_eq_myersonPayment_of_isDSIC_of_zeroNormalized
---

# paymentRule_eq_virtualSurplusMaximizingPaymentRule_of_isDSIC_of_zeroNormalized

## Lean type

```lean
theorem paymentRule_eq_virtualSurplusMaximizingPaymentRule_of_isDSIC_of_zeroNormalized [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {p : (I → ℝ) → I → ℝ} (hdsic : ({ allocationRule
```

## Dependencies

- IsDSIC
- isDSIC
- ZeroNormalized
- payment_eq_myersonPayment_of_isDSIC_of_zeroNormalized
