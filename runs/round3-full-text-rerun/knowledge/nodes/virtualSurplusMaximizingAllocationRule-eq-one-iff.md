---
id: virtualSurplusMaximizingAllocationRule-eq-one-iff
title: virtualSurplusMaximizingAllocationRule_eq_one_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_eq_one_iff
uses:
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# virtualSurplusMaximizingAllocationRule_eq_one_iff

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_eq_one_iff [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) (i : I) : A.virtualSurplusMaximizingAllocationRule b i = 1 ↔ 0 < A.winningVirtualValue b ∧ i = A.virtualSurplusMaximizingWinner b
```

## Dependencies

- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- IsPositiveAffineOf.symm
- Indifferent.symm
