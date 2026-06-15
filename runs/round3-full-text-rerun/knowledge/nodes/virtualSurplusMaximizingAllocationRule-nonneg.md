---
id: virtualSurplusMaximizingAllocationRule-nonneg
title: virtualSurplusMaximizingAllocationRule_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_nonneg
uses:
---

# virtualSurplusMaximizingAllocationRule_nonneg

## Lean type

```lean
lemma virtualSurplusMaximizingAllocationRule_nonneg [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) (i : I) : 0 ≤ A.virtualSurplusMaximizingAllocationRule b i
```

## Dependencies

- none
