---
id: virtualSurplusMaximizingAllocationRule-eq-zero-of-forall-virtualValue-nonpos
title: virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_virtualValue_nonpos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_virtualValue_nonpos
uses:
---

# virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_virtualValue_nonpos

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_virtualValue_nonpos [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {b : I → ℝ} (hnonpos : ∀ i, A.virtualValue i (b i) ≤ 0) : A.virtualSurplusMaximizingAllocationRule b = fun _ => (0 : ℝ)
```

## Dependencies

- none
