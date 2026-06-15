---
id: hasIntegrableInterimObjects-of-aestronglyMeasurable-of-bound
title: hasIntegrableInterimObjects_of_aestronglyMeasurable_of_bound
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasIntegrableInterimObjects_of_aestronglyMeasurable_of_bound
uses:
  - HasIntegrableInterimObjects
  - hasIntegrableInterimAllocation_of_aestronglyMeasurable_of_bound
  - hasIntegrableInterimPayment_of_aestronglyMeasurable_of_bound
---

# hasIntegrableInterimObjects_of_aestronglyMeasurable_of_bound

## Lean type

```lean
theorem hasIntegrableInterimObjects_of_aestronglyMeasurable_of_bound (A : BayesianSingleItemAuction I) (halloc_meas : ∀ i z_i, AEStronglyMeasurable (fun t => A.interimAllocationIntegrand i z_i t) (A.opponentPrior i)) (hpay_meas : ∀ i z_i, AEStronglyMeasurable (fun t => A.interimPaymentIntegrand i z_i t) (A.opponentPrior i)) (halloc_bound : ∀ i z_i, ∃ C : ℝ, ∀ᵐ t ∂A.opponentPrior i, ‖A.interimAllocationIntegrand i z_i t‖ ≤ C) (hpay_bound : ∀ i z_i, ∃ C : ℝ, ∀ᵐ t ∂A.opponentPrior i, ‖A.interimPaymentIntegrand i z_i t‖ ≤ C) : A.HasIntegrableInterimObjects
```

## Dependencies

- HasIntegrableInterimObjects
- hasIntegrableInterimAllocation_of_aestronglyMeasurable_of_bound
- hasIntegrableInterimPayment_of_aestronglyMeasurable_of_bound
