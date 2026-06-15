---
id: withMyersonPayment-isDSIC-of-isMonotone
title: withMyersonPayment_isDSIC_of_isMonotone
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - withMyersonPayment_isDSIC_of_isMonotone
uses:
  - IsMonotone
  - IsDSIC
  - isDSIC
  - quasiLinearUtility
  - withMyersonPayment_quasiLinearUtility_eq
---

# withMyersonPayment_isDSIC_of_isMonotone

## Lean type

```lean
theorem withMyersonPayment_isDSIC_of_isMonotone [DecidableEq I] {x : (I → ℝ) → I → ℝ} (hx : IsMonotone ({ allocationRule
```

## Dependencies

- IsMonotone
- IsDSIC
- isDSIC
- quasiLinearUtility
- withMyersonPayment_quasiLinearUtility_eq
