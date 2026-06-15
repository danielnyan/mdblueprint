---
id: IsSingleItemAllocationRule-le-one
title: IsSingleItemAllocationRule.le_one
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsSingleItemAllocationRule.le_one
uses:
  - IsFeasible.isSingleItemAllocationRule
  - IsSingleItemAllocationRule
---

# IsSingleItemAllocationRule.le_one

## Lean type

```lean
theorem IsSingleItemAllocationRule.le_one [Fintype I] [DecidableEq I] {x : (I → ℝ) → I → ℝ} (hx : IsSingleItemAllocationRule x) (b : I → ℝ) (i : I) : x b i ≤ 1
```

## Dependencies

- IsFeasible.isSingleItemAllocationRule
- IsSingleItemAllocationRule
