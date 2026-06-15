---
id: hasIntegrableInterimAllocation-of-isFeasible-of-aestronglyMeasurable
title: hasIntegrableInterimAllocation_of_isFeasible_of_aestronglyMeasurable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasIntegrableInterimAllocation_of_isFeasible_of_aestronglyMeasurable
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - HasIntegrableInterimAllocation
  - hasIntegrableInterimAllocation_of_aestronglyMeasurable_of_bound
---

# hasIntegrableInterimAllocation_of_isFeasible_of_aestronglyMeasurable

## Lean type

```lean
theorem hasIntegrableInterimAllocation_of_isFeasible_of_aestronglyMeasurable [Fintype I] (A : BayesianSingleItemAuction I) (hfeas : A.IsFeasible) (hmeas : ∀ i z_i, AEStronglyMeasurable (fun t => A.interimAllocationIntegrand i z_i t) (A.opponentPrior i)) : A.HasIntegrableInterimAllocation
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- HasIntegrableInterimAllocation
- hasIntegrableInterimAllocation_of_aestronglyMeasurable_of_bound
