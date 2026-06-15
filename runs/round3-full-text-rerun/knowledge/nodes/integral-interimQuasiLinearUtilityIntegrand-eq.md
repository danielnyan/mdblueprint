---
id: integral-interimQuasiLinearUtilityIntegrand-eq
title: integral_interimQuasiLinearUtilityIntegrand_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integral_interimQuasiLinearUtilityIntegrand_eq
uses:
  - HasIntegrableInterimAllocation
  - HasIntegrableInterimPayment
---

# integral_interimQuasiLinearUtilityIntegrand_eq

## Lean type

```lean
theorem integral_interimQuasiLinearUtilityIntegrand_eq (A : BayesianSingleItemAuction I) (hQ : A.HasIntegrableInterimAllocation) (hM : A.HasIntegrableInterimPayment) (i : I) (t_i z_i : ℝ) : (∫ t, A.interimQuasiLinearUtilityIntegrand i t_i z_i t ∂A.opponentPrior i) = A.interimQuasiLinearUtility i t_i z_i
```

## Dependencies

- HasIntegrableInterimAllocation
- HasIntegrableInterimPayment
