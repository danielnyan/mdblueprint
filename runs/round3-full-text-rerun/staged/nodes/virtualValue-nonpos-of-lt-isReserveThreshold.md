---
id: virtualValue-nonpos-of-lt-isReserveThreshold
title: virtualValue_nonpos_of_lt_isReserveThreshold
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualValue_nonpos_of_lt_isReserveThreshold
uses:
  - IsReserveThreshold
---

# virtualValue_nonpos_of_lt_isReserveThreshold

## Lean type

```lean
theorem virtualValue_nonpos_of_lt_isReserveThreshold (A : BayesianSingleItemAuction I) {i : I} {reserve v : ℝ} (hreserve : A.IsReserveThreshold i reserve) (hv : v < reserve) : A.virtualValue i v ≤ 0
```

## Dependencies

- IsReserveThreshold
