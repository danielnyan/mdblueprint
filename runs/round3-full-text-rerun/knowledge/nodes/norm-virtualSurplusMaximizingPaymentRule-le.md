---
id: norm-virtualSurplusMaximizingPaymentRule-le
title: norm_virtualSurplusMaximizingPaymentRule_le
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - norm_virtualSurplusMaximizingPaymentRule_le
uses:
  - virtualSurplusMaximizingAllocationRule_nonneg
  - virtualSurplusMaximizingAllocationRule_le_one
---

# norm_virtualSurplusMaximizingPaymentRule_le

## Lean type

```lean
theorem norm_virtualSurplusMaximizingPaymentRule_le [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (b : I → ℝ) (i : I) : ‖A.virtualSurplusMaximizingPaymentRule b i‖ ≤ 2 * ‖b i‖
```

## Dependencies

- virtualSurplusMaximizingAllocationRule_nonneg
- virtualSurplusMaximizingAllocationRule_le_one
