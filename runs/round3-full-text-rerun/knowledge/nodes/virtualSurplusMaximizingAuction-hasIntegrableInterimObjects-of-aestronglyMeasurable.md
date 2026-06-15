---
id: virtualSurplusMaximizingAuction-hasIntegrableInterimObjects-of-aestronglyMeasurable
title: virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_aestronglyMeasurable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_aestronglyMeasurable
uses:
  - HasIntegrableInterimObjects
  - hasIntegrableInterimObjects_of_aestronglyMeasurable_of_bound
  - virtualSurplusMaximizingAuction_isFeasible
  - virtualSurplusMaximizingAuction_interimPaymentIntegrand_bound
---

# virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_aestronglyMeasurable

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_aestronglyMeasurable [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (halloc_meas : ∀ i z_i, AEStronglyMeasurable (fun t => A.virtualSurplusMaximizingAuction.interimAllocationIntegrand i z_i t) (A.opponentPrior i)) (hpay_meas : ∀ i z_i, AEStronglyMeasurable (fun t => A.virtualSurplusMaximizingAuction.interimPaymentIntegrand i z_i t) (A.opponentPrior i)) : A.virtualSurplusMaximizingAuction.HasIntegrableInterimObjects
```

## Dependencies

- HasIntegrableInterimObjects
- hasIntegrableInterimObjects_of_aestronglyMeasurable_of_bound
- virtualSurplusMaximizingAuction_isFeasible
- virtualSurplusMaximizingAuction_interimPaymentIntegrand_bound
