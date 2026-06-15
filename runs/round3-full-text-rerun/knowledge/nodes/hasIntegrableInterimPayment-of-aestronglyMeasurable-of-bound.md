---
id: hasIntegrableInterimPayment-of-aestronglyMeasurable-of-bound
title: hasIntegrableInterimPayment_of_aestronglyMeasurable_of_bound
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasIntegrableInterimPayment_of_aestronglyMeasurable_of_bound
uses:
  - HasIntegrableInterimPayment
---

# hasIntegrableInterimPayment_of_aestronglyMeasurable_of_bound

## Lean type

```lean
theorem hasIntegrableInterimPayment_of_aestronglyMeasurable_of_bound (A : BayesianSingleItemAuction I) (hmeas : ∀ i z_i, AEStronglyMeasurable (fun t => A.interimPaymentIntegrand i z_i t) (A.opponentPrior i)) (hbound : ∀ i z_i, ∃ C : ℝ, ∀ᵐ t ∂A.opponentPrior i, ‖A.interimPaymentIntegrand i z_i t‖ ≤ C) : A.HasIntegrableInterimPayment
```

## Dependencies

- HasIntegrableInterimPayment
