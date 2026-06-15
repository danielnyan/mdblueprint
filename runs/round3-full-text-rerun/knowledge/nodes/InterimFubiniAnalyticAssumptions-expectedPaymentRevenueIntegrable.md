---
id: InterimFubiniAnalyticAssumptions-expectedPaymentRevenueIntegrable
title: InterimFubiniAnalyticAssumptions.expectedPaymentRevenueIntegrable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - InterimFubiniAnalyticAssumptions.expectedPaymentRevenueIntegrable
uses:
  - PaymentInterimFubiniAssumptions.expectedPaymentRevenueIntegrable
---

# InterimFubiniAnalyticAssumptions.expectedPaymentRevenueIntegrable

## Lean type

```lean
theorem InterimFubiniAnalyticAssumptions.expectedPaymentRevenueIntegrable [Fintype I] {A B : BayesianSingleItemAuction I} (h : A.InterimFubiniAnalyticAssumptions B) : Integrable (fun t => ∑ i, B.paymentRule t i) A.prior
```

## Dependencies

- PaymentInterimFubiniAssumptions.expectedPaymentRevenueIntegrable
