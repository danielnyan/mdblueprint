---
id: expectedSellerRevenueInEnvironment-eq-myersonPaymentRevenueInEnvironment-of-isDSIC-of-isZeroNormalized
title: expectedSellerRevenueInEnvironment_eq_myersonPaymentRevenueInEnvironment_of_isDSIC_of_isZeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - expectedSellerRevenueInEnvironment_eq_myersonPaymentRevenueInEnvironment_of_isDSIC_of_isZeroNormalized
uses:
  - IsDSIC
  - isDSIC
  - IsZeroNormalized
  - paymentRule_eq_myersonPayment_of_isDSIC_of_isZeroNormalized
---

# expectedSellerRevenueInEnvironment_eq_myersonPaymentRevenueInEnvironment_of_isDSIC_of_isZeroNormalized

## Lean type

```lean
theorem expectedSellerRevenueInEnvironment_eq_myersonPaymentRevenueInEnvironment_of_isDSIC_of_isZeroNormalized [Fintype I] [DecidableEq I] (A B : BayesianSingleItemAuction I) (hdsic : B.IsDSIC) (hzero : B.IsZeroNormalized) : A.expectedSellerRevenueInEnvironment B = A.myersonPaymentRevenueInEnvironment B
```

## Dependencies

- IsDSIC
- isDSIC
- IsZeroNormalized
- paymentRule_eq_myersonPayment_of_isDSIC_of_isZeroNormalized
