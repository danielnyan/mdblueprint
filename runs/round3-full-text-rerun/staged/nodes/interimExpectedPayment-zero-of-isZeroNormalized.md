---
id: interimExpectedPayment-zero-of-isZeroNormalized
title: interimExpectedPayment_zero_of_isZeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - interimExpectedPayment_zero_of_isZeroNormalized
uses:
  - IsZeroNormalized
  - OpponentTypeProfile
  - ZeroNormalized
  - interimExpectedPayment_eq_integral_interimPaymentIntegrand
---

# interimExpectedPayment_zero_of_isZeroNormalized

## Lean type

```lean
theorem interimExpectedPayment_zero_of_isZeroNormalized [DecidableEq I] (B : BayesianSingleItemAuction I) (hzero : B.IsZeroNormalized) (i : I) : B.interimExpectedPayment i 0 = 0
```

## Dependencies

- IsZeroNormalized
- OpponentTypeProfile
- ZeroNormalized
- interimExpectedPayment_eq_integral_interimPaymentIntegrand
