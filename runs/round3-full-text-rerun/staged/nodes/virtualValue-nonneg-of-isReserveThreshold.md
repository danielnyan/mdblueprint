---
id: virtualValue-nonneg-of-isReserveThreshold
title: virtualValue_nonneg_of_isReserveThreshold
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualValue_nonneg_of_isReserveThreshold
uses:
  - IsReserveThreshold
---

# virtualValue_nonneg_of_isReserveThreshold

## Lean type

```lean
theorem virtualValue_nonneg_of_isReserveThreshold (A : BayesianSingleItemAuction I) {i : I} {reserve v : ℝ} (hreserve : A.IsReserveThreshold i reserve) (hv : reserve ≤ v) : 0 ≤ A.virtualValue i v
```

## Dependencies

- IsReserveThreshold
