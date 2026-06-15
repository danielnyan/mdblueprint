---
id: integrable-interimQuasiLinearUtilityIntegrand
title: integrable_interimQuasiLinearUtilityIntegrand
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - integrable_interimQuasiLinearUtilityIntegrand
uses:
  - HasIntegrableInterimAllocation
  - HasIntegrableInterimPayment
---

# integrable_interimQuasiLinearUtilityIntegrand

## Lean type

```lean
theorem integrable_interimQuasiLinearUtilityIntegrand (A : BayesianSingleItemAuction I) (hQ : A.HasIntegrableInterimAllocation) (hM : A.HasIntegrableInterimPayment) (i : I) (t_i z_i : ℝ) : Integrable (fun t => A.interimQuasiLinearUtilityIntegrand i t_i z_i t) (A.opponentPrior i)
```

## Dependencies

- HasIntegrableInterimAllocation
- HasIntegrableInterimPayment
