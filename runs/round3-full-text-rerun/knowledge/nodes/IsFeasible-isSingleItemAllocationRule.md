---
id: IsFeasible-isSingleItemAllocationRule
title: IsFeasible.isSingleItemAllocationRule
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsFeasible.isSingleItemAllocationRule
uses:
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsSingleItemAllocationRule
  - Profile.ext
  - virtualSurplusMaximizingWinner_eq_iff_forall_virtualScore_le
  - winningVirtualValue_pos_iff_exists_virtualValue_pos
  - OpponentTypeProfile
---

# IsFeasible.isSingleItemAllocationRule

## Lean type

```lean
theorem IsFeasible.isSingleItemAllocationRule [Fintype I] {B : BayesianSingleItemAuction I} (hB : B.IsFeasible) : IsSingleItemAllocationRule B.allocationRule
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsSingleItemAllocationRule
- Profile.ext
- virtualSurplusMaximizingWinner_eq_iff_forall_virtualScore_le
- winningVirtualValue_pos_iff_exists_virtualValue_pos
- OpponentTypeProfile
