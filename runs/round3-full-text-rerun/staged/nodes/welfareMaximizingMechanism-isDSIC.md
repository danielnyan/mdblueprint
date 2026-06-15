---
id: welfareMaximizingMechanism-isDSIC
title: welfareMaximizingMechanism_isDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - welfareMaximizingMechanism_isDSIC
uses:
  - IsDSIC
  - isDSIC
  - withMyersonPayment_isDSIC_of_isMonotone
  - welfareMaximizingAllocationRule_isMonotone
---

# welfareMaximizingMechanism_isDSIC

## Lean type

```lean
theorem welfareMaximizingMechanism_isDSIC (A : KnapsackAuction I ℝ) (hW : 0 ≤ A.totalCapacity) : (A.welfareMaximizingMechanism hW).IsDSIC
```

## Dependencies

- IsDSIC
- isDSIC
- withMyersonPayment_isDSIC_of_isMonotone
- welfareMaximizingAllocationRule_isMonotone
