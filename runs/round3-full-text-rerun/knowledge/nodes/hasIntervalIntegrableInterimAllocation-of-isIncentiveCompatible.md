---
id: hasIntervalIntegrableInterimAllocation-of-isIncentiveCompatible
title: hasIntervalIntegrableInterimAllocation_of_isIncentiveCompatible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - hasIntervalIntegrableInterimAllocation_of_isIncentiveCompatible
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - HasIntervalIntegrableInterimAllocation
  - interimAllocProb_mono_of_isIncentiveCompatible
---

# hasIntervalIntegrableInterimAllocation_of_isIncentiveCompatible

## Lean type

```lean
theorem hasIntervalIntegrableInterimAllocation_of_isIncentiveCompatible (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) : A.HasIntervalIntegrableInterimAllocation
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- HasIntervalIntegrableInterimAllocation
- interimAllocProb_mono_of_isIncentiveCompatible
