---
id: hasNonnegativeInterimAllocationIntegralOnSupport-of-isFeasible
title: hasNonnegativeInterimAllocationIntegralOnSupport_of_isFeasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasNonnegativeInterimAllocationIntegralOnSupport_of_isFeasible
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - HasNonnegativeInterimAllocationIntegralOnSupport
  - interimAllocProb_nonneg_of_isFeasible
---

# hasNonnegativeInterimAllocationIntegralOnSupport_of_isFeasible

## Lean type

```lean
theorem hasNonnegativeInterimAllocationIntegralOnSupport_of_isFeasible [Fintype I] (A : BayesianSingleItemAuction I) (hfeas : A.IsFeasible) : A.HasNonnegativeInterimAllocationIntegralOnSupport
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- HasNonnegativeInterimAllocationIntegralOnSupport
- interimAllocProb_nonneg_of_isFeasible
