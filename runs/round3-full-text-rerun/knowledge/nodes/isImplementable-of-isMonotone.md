---
id: isImplementable-of-isMonotone
title: isImplementable_of_isMonotone
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - isImplementable_of_isMonotone
uses:
  - IsMonotone
  - IsImplementable
  - withMyersonPayment_isDSIC_of_isMonotone
---

# isImplementable_of_isMonotone

## Lean type

```lean
theorem isImplementable_of_isMonotone [DecidableEq I] {x : (I → ℝ) → I → ℝ} (hx : IsMonotone ({ allocationRule
```

## Dependencies

- IsMonotone
- IsImplementable
- withMyersonPayment_isDSIC_of_isMonotone
