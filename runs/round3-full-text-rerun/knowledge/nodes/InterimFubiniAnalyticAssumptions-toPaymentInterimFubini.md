---
id: InterimFubiniAnalyticAssumptions-toPaymentInterimFubini
title: InterimFubiniAnalyticAssumptions.toPaymentInterimFubini
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - InterimFubiniAnalyticAssumptions.toPaymentInterimFubini
uses:
---

# InterimFubiniAnalyticAssumptions.toPaymentInterimFubini

## Lean type

```lean
theorem InterimFubiniAnalyticAssumptions.toPaymentInterimFubini [Fintype I] {A B : BayesianSingleItemAuction I} (h : A.InterimFubiniAnalyticAssumptions B) : A.PaymentInterimFubiniAssumptions B
```

## Dependencies

- none
