---
id: winningVirtualValue-pos-iff-exists-virtualValue-pos
title: winningVirtualValue_pos_iff_exists_virtualValue_pos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - winningVirtualValue_pos_iff_exists_virtualValue_pos
uses:
  - virtualSurplusMaximizingWinner_virtualValue_ge
---

# winningVirtualValue_pos_iff_exists_virtualValue_pos

## Lean type

```lean
theorem winningVirtualValue_pos_iff_exists_virtualValue_pos [Fintype I] [Nontrivial I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) : 0 < A.winningVirtualValue b ↔ ∃ i, 0 < A.virtualValue i (b i)
```

## Dependencies

- virtualSurplusMaximizingWinner_virtualValue_ge
