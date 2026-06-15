---
id: InterimFubiniAnalyticAssumptions-hasExpectedRevenueInterimPaymentIdentity
title: InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
uses:
  - PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
  - HasExpectedRevenueInterimPaymentIdentity
---

# InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity

## Lean type

```lean
theorem InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity [Fintype I] {A B : BayesianSingleItemAuction I} (h : A.InterimFubiniAnalyticAssumptions B) : A.HasExpectedRevenueInterimPaymentIdentity B
```

## Dependencies

- PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
- HasExpectedRevenueInterimPaymentIdentity
