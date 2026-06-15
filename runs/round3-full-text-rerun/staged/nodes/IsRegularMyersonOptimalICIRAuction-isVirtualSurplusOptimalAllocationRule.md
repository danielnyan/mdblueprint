---
id: IsRegularMyersonOptimalICIRAuction-isVirtualSurplusOptimalAllocationRule
title: IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule
uses:
  - IsRegularMyersonOptimalICIRAuction
  - IsVirtualSurplusOptimalAllocationRule
---

# IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule

## Lean type

```lean
theorem IsRegularMyersonOptimalICIRAuction.isVirtualSurplusOptimalAllocationRule [Fintype I] {A B : BayesianSingleItemAuction I} (hB : A.IsRegularMyersonOptimalICIRAuction B) : A.IsVirtualSurplusOptimalAllocationRule B.allocationRule
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction
- IsVirtualSurplusOptimalAllocationRule
