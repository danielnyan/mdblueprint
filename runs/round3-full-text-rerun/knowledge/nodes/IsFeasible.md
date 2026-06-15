---
id: IsFeasible
title: IsFeasible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - IsFeasible
uses:
  - rowEval
  - Valuation
  - CombinatorialAllocation
  - MultiItemBundle
  - toFinset
  - IsAllocFeasible
  - RespectsSingleItemCapacity
  - OpponentTypeProfile
  - IsAllocFeasible
  - RespectsCapacity
---

# IsFeasible

## Lean type

```lean
def IsFeasible [Fintype I] (A : KnapsackAuction I U) : Prop
```

## Dependencies

- rowEval
- Valuation
- CombinatorialAllocation
- MultiItemBundle
- toFinset
- IsAllocFeasible
- RespectsSingleItemCapacity
- OpponentTypeProfile
- IsAllocFeasible
- RespectsCapacity
