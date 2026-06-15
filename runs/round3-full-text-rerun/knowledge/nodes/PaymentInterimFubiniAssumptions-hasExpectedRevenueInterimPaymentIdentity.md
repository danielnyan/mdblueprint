---
id: PaymentInterimFubiniAssumptions-hasExpectedRevenueInterimPaymentIdentity
title: PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
uses:
  - InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
  - HasExpectedRevenueInterimPaymentIdentity
---

# PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity

## Lean type

```lean
theorem PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity [Fintype I] {A B : BayesianSingleItemAuction I} (h : A.PaymentInterimFubiniAssumptions B) : A.HasExpectedRevenueInterimPaymentIdentity B
```

## Dependencies

- InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
- HasExpectedRevenueInterimPaymentIdentity
