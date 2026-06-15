---
id: interimExpectedPayment-eq-integral-interimPaymentIntegrand
title: interimExpectedPayment_eq_integral_interimPaymentIntegrand
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimExpectedPayment_eq_integral_interimPaymentIntegrand
uses:
---

# interimExpectedPayment_eq_integral_interimPaymentIntegrand

## Lean type

```lean
theorem interimExpectedPayment_eq_integral_interimPaymentIntegrand (A : BayesianSingleItemAuction I) (i : I) (z_i : ℝ) : A.interimExpectedPayment i z_i = ∫ t, A.interimPaymentIntegrand i z_i t ∂A.opponentPrior i
```

## Dependencies

- none
