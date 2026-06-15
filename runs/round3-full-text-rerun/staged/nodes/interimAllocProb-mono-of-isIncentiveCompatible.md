---
id: interimAllocProb-mono-of-isIncentiveCompatible
title: interimAllocProb_mono_of_isIncentiveCompatible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimAllocProb_mono_of_isIncentiveCompatible
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
---

# interimAllocProb_mono_of_isIncentiveCompatible

## Lean type

```lean
theorem interimAllocProb_mono_of_isIncentiveCompatible (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) (i : I) : Monotone (A.interimAllocProb i)
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
