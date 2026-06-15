---
id: virtualSurplusMaximizingAllocationRule-le-one
title: virtualSurplusMaximizingAllocationRule_le_one
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_le_one
uses:
---

# virtualSurplusMaximizingAllocationRule_le_one

## Lean type

```lean
lemma virtualSurplusMaximizingAllocationRule_le_one [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) (i : I) : A.virtualSurplusMaximizingAllocationRule b i ≤ 1
```

## Dependencies

- none
