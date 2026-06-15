---
id: virtualSurplusMaximizingAllocationRule-respectsSingleItemCapacity
title: virtualSurplusMaximizingAllocationRule_respectsSingleItemCapacity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_respectsSingleItemCapacity
uses:
---

# virtualSurplusMaximizingAllocationRule_respectsSingleItemCapacity

## Lean type

```lean
lemma virtualSurplusMaximizingAllocationRule_respectsSingleItemCapacity [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) : (∑ i, A.virtualSurplusMaximizingAllocationRule b i) ≤ 1
```

## Dependencies

- none
