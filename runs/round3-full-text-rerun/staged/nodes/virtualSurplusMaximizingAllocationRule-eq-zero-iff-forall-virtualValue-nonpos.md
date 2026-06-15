---
id: virtualSurplusMaximizingAllocationRule-eq-zero-iff-forall-virtualValue-nonpos
title: virtualSurplusMaximizingAllocationRule_eq_zero_iff_forall_virtualValue_nonpos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_eq_zero_iff_forall_virtualValue_nonpos
uses:
  - winningVirtualValue_nonpos_iff_forall_virtualValue_nonpos
  - virtualSurplusMaximizingAllocationRule_winner_eq_one_of_winningVirtualValue_pos
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_virtualValue_nonpos
---

# virtualSurplusMaximizingAllocationRule_eq_zero_iff_forall_virtualValue_nonpos

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_eq_zero_iff_forall_virtualValue_nonpos [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {b : I → ℝ} : (A.virtualSurplusMaximizingAllocationRule b = fun _ => (0 : ℝ)) ↔ ∀ i, A.virtualValue i (b i) ≤ 0
```

## Dependencies

- winningVirtualValue_nonpos_iff_forall_virtualValue_nonpos
- virtualSurplusMaximizingAllocationRule_winner_eq_one_of_winningVirtualValue_pos
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_virtualValue_nonpos
