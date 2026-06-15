---
id: exists-virtualSurplusMaximizingAllocationRule-eq-one-iff-exists-virtualValue-pos
title: exists_virtualSurplusMaximizingAllocationRule_eq_one_iff_exists_virtualValue_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - exists_virtualSurplusMaximizingAllocationRule_eq_one_iff_exists_virtualValue_pos
uses:
  - virtualValue_pos_of_virtualSurplusMaximizingAllocationRule_eq_one
  - winningVirtualValue_pos_iff_exists_virtualValue_pos
  - virtualSurplusMaximizingAllocationRule_winner_eq_one_of_winningVirtualValue_pos
---

# exists_virtualSurplusMaximizingAllocationRule_eq_one_iff_exists_virtualValue_pos

## Lean type

```lean
theorem exists_virtualSurplusMaximizingAllocationRule_eq_one_iff_exists_virtualValue_pos [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) : (∃ i, A.virtualSurplusMaximizingAllocationRule b i = 1) ↔ ∃ i, 0 < A.virtualValue i (b i)
```

## Dependencies

- virtualValue_pos_of_virtualSurplusMaximizingAllocationRule_eq_one
- winningVirtualValue_pos_iff_exists_virtualValue_pos
- virtualSurplusMaximizingAllocationRule_winner_eq_one_of_winningVirtualValue_pos
