---
id: exists-virtualSurplusMaximizingAllocationRule-eq-one-iff-winningVirtualValue-pos
title: exists_virtualSurplusMaximizingAllocationRule_eq_one_iff_winningVirtualValue_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - exists_virtualSurplusMaximizingAllocationRule_eq_one_iff_winningVirtualValue_pos
uses:
  - exists_virtualSurplusMaximizingAllocationRule_eq_one_iff_exists_virtualValue_pos
  - winningVirtualValue_pos_iff_exists_virtualValue_pos
---

# exists_virtualSurplusMaximizingAllocationRule_eq_one_iff_winningVirtualValue_pos

## Lean type

```lean
theorem exists_virtualSurplusMaximizingAllocationRule_eq_one_iff_winningVirtualValue_pos [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) : (∃ i, A.virtualSurplusMaximizingAllocationRule b i = 1) ↔ 0 < A.winningVirtualValue b
```

## Dependencies

- exists_virtualSurplusMaximizingAllocationRule_eq_one_iff_exists_virtualValue_pos
- winningVirtualValue_pos_iff_exists_virtualValue_pos
