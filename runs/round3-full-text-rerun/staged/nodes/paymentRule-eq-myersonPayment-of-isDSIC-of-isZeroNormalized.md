---
id: paymentRule-eq-myersonPayment-of-isDSIC-of-isZeroNormalized
title: paymentRule_eq_myersonPayment_of_isDSIC_of_isZeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - paymentRule_eq_myersonPayment_of_isDSIC_of_isZeroNormalized
uses:
  - IsDSIC
  - isDSIC
  - IsZeroNormalized
  - payment_eq_myersonPayment_of_isDSIC_of_zeroNormalized
---

# paymentRule_eq_myersonPayment_of_isDSIC_of_isZeroNormalized

## Lean type

```lean
theorem paymentRule_eq_myersonPayment_of_isDSIC_of_isZeroNormalized [Fintype I] [DecidableEq I] (B : BayesianSingleItemAuction I) (hdsic : B.IsDSIC) (hzero : B.IsZeroNormalized) : B.paymentRule = SingleParameterMechanism.myersonPayment B.allocationRule
```

## Dependencies

- IsDSIC
- isDSIC
- IsZeroNormalized
- payment_eq_myersonPayment_of_isDSIC_of_zeroNormalized
