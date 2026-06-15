---
id: virtualSurplusMaximizingAllocationRule-eq-zero-of-forall-lt-reserveThreshold
title: virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_lt_reserveThreshold
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_lt_reserveThreshold
uses:
  - IsReserveThreshold
  - virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_virtualValue_nonpos
  - virtualValue_nonpos_of_lt_isReserveThreshold
---

# virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_lt_reserveThreshold

## Lean type

```lean
theorem virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_lt_reserveThreshold [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) {reserve b : I → ℝ} (hreserve : ∀ i, A.IsReserveThreshold i (reserve i)) (hb : ∀ i, b i < reserve i) : A.virtualSurplusMaximizingAllocationRule b = fun _ => (0 : ℝ)
```

## Dependencies

- IsReserveThreshold
- virtualSurplusMaximizingAllocationRule_eq_zero_of_forall_virtualValue_nonpos
- virtualValue_nonpos_of_lt_isReserveThreshold
