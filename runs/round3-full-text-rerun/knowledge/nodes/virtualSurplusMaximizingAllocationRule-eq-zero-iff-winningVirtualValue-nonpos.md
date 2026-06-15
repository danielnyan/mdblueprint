---
id: virtualSurplusMaximizingAllocationRule-eq-zero-iff-winningVirtualValue-nonpos
title: virtualSurplusMaximizingAllocationRule_eq_zero_iff_winningVirtualValue_nonpos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_eq_zero_iff_winningVirtualValue_nonpos
uses:
  - winningVirtualValue_nonpos_iff_forall_virtualValue_nonpos
---

# virtualSurplusMaximizingAllocationRule_eq_zero_iff_winningVirtualValue_nonpos

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_eq_zero_iff_winningVirtualValue_nonpos [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {b : I → ℝ} : (A.virtualSurplusMaximizingAllocationRule b = fun _ => (0 : ℝ)) ↔ A.winningVirtualValue b ≤ 0
```

## Dependencies

- winningVirtualValue_nonpos_iff_forall_virtualValue_nonpos
