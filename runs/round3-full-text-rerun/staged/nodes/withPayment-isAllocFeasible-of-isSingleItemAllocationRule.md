---
id: withPayment-isAllocFeasible-of-isSingleItemAllocationRule
title: withPayment_isAllocFeasible_of_isSingleItemAllocationRule
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - withPayment_isAllocFeasible_of_isSingleItemAllocationRule
uses:
  - IsFeasible.isSingleItemAllocationRule
  - IsSingleItemAllocationRule
  - IsAllocFeasible
  - IsSingleItemAllocationRule.le_one
---

# withPayment_isAllocFeasible_of_isSingleItemAllocationRule

## Lean type

```lean
theorem withPayment_isAllocFeasible_of_isSingleItemAllocationRule [Fintype I] [DecidableEq I] {x p : (I → ℝ) → I → ℝ} (hx : IsSingleItemAllocationRule x) : ({ allocationRule
```

## Dependencies

- IsFeasible.isSingleItemAllocationRule
- IsSingleItemAllocationRule
- IsAllocFeasible
- IsSingleItemAllocationRule.le_one
