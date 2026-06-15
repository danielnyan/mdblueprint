---
id: hasIntegrableInterimAllocation-of-aestronglyMeasurable-of-bound
title: hasIntegrableInterimAllocation_of_aestronglyMeasurable_of_bound
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasIntegrableInterimAllocation_of_aestronglyMeasurable_of_bound
uses:
  - HasIntegrableInterimAllocation
---

# hasIntegrableInterimAllocation_of_aestronglyMeasurable_of_bound

## Lean type

```lean
theorem hasIntegrableInterimAllocation_of_aestronglyMeasurable_of_bound (A : BayesianSingleItemAuction I) (hmeas : ∀ i z_i, AEStronglyMeasurable (fun t => A.interimAllocationIntegrand i z_i t) (A.opponentPrior i)) (hbound : ∀ i z_i, ∃ C : ℝ, ∀ᵐ t ∂A.opponentPrior i, ‖A.interimAllocationIntegrand i z_i t‖ ≤ C) : A.HasIntegrableInterimAllocation
```

## Dependencies

- HasIntegrableInterimAllocation
