---
id: PaymentInterimFubiniAssumptions-expectedPaymentRevenueIntegrable
title: PaymentInterimFubiniAssumptions.expectedPaymentRevenueIntegrable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - PaymentInterimFubiniAssumptions.expectedPaymentRevenueIntegrable
uses:
---

# PaymentInterimFubiniAssumptions.expectedPaymentRevenueIntegrable

## Lean type

```lean
theorem PaymentInterimFubiniAssumptions.expectedPaymentRevenueIntegrable [Fintype I] {A B : BayesianSingleItemAuction I} (h : A.PaymentInterimFubiniAssumptions B) : Integrable (fun t => ∑ i, B.paymentRule t i) A.prior
```

## Dependencies

- none
