---
id: virtualValue-pos-of-virtualSurplusMaximizingAllocationRule-eq-one
title: virtualValue_pos_of_virtualSurplusMaximizingAllocationRule_eq_one
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualValue_pos_of_virtualSurplusMaximizingAllocationRule_eq_one
uses:
  - virtualSurplusMaximizingAllocationRule_eq_one_iff
---

# virtualValue_pos_of_virtualSurplusMaximizingAllocationRule_eq_one

## Lean type

```lean
theorem virtualValue_pos_of_virtualSurplusMaximizingAllocationRule_eq_one [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {b : I → ℝ} {i : I} (hi : A.virtualSurplusMaximizingAllocationRule b i = 1) : 0 < A.virtualValue i (b i)
```

## Dependencies

- virtualSurplusMaximizingAllocationRule_eq_one_iff
