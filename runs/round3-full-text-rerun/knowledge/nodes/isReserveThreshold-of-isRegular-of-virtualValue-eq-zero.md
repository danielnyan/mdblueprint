---
id: isReserveThreshold-of-isRegular-of-virtualValue-eq-zero
title: isReserveThreshold_of_isRegular_of_virtualValue_eq_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - isReserveThreshold_of_isRegular_of_virtualValue_eq_zero
uses:
  - IsRegular
  - IsReserveThreshold
---

# isReserveThreshold_of_isRegular_of_virtualValue_eq_zero

## Lean type

```lean
theorem isReserveThreshold_of_isRegular_of_virtualValue_eq_zero (A : BayesianSingleItemAuction I) (hA : A.IsRegular) {i : I} {reserve : ℝ} (hzero : A.virtualValue i reserve = 0) : A.IsReserveThreshold i reserve
```

## Dependencies

- IsRegular
- IsReserveThreshold
