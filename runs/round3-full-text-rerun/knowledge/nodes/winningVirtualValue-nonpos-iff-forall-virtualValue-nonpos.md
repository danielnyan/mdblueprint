---
id: winningVirtualValue-nonpos-iff-forall-virtualValue-nonpos
title: winningVirtualValue_nonpos_iff_forall_virtualValue_nonpos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - winningVirtualValue_nonpos_iff_forall_virtualValue_nonpos
uses:
  - virtualSurplusMaximizingWinner_virtualValue_ge
---

# winningVirtualValue_nonpos_iff_forall_virtualValue_nonpos

## Lean type

```lean
theorem winningVirtualValue_nonpos_iff_forall_virtualValue_nonpos [Fintype I] [Nontrivial I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) : A.winningVirtualValue b ≤ 0 ↔ ∀ i, A.virtualValue i (b i) ≤ 0
```

## Dependencies

- virtualSurplusMaximizingWinner_virtualValue_ge
