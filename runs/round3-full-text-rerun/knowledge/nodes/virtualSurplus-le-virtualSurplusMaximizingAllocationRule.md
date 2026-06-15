---
id: virtualSurplus-le-virtualSurplusMaximizingAllocationRule
title: virtualSurplus_le_virtualSurplusMaximizingAllocationRule
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplus_le_virtualSurplusMaximizingAllocationRule
uses:
---

# virtualSurplus_le_virtualSurplusMaximizingAllocationRule

## Lean type

```lean
theorem virtualSurplus_le_virtualSurplusMaximizingAllocationRule [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {x : (I → ℝ) → I → ℝ} {b : I → ℝ} (hx_nonneg : ∀ i, 0 ≤ x b i) (hx_capacity : (∑ i, x b i) ≤ 1) : A.virtualSurplus x b ≤ A.virtualSurplus A.virtualSurplusMaximizingAllocationRule b
```

## Dependencies

- none
