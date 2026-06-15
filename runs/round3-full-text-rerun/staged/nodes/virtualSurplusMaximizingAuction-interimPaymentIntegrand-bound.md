---
id: virtualSurplusMaximizingAuction-interimPaymentIntegrand-bound
title: virtualSurplusMaximizingAuction_interimPaymentIntegrand_bound
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_interimPaymentIntegrand_bound
uses:
  - norm_virtualSurplusMaximizingPaymentRule_le
---

# virtualSurplusMaximizingAuction_interimPaymentIntegrand_bound

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_interimPaymentIntegrand_bound [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (i : I) (z_i : ℝ) : ∀ᵐ t ∂A.opponentPrior i, ‖A.virtualSurplusMaximizingAuction.interimPaymentIntegrand i z_i t‖ ≤ 2 * ‖z_i‖
```

## Dependencies

- norm_virtualSurplusMaximizingPaymentRule_le
