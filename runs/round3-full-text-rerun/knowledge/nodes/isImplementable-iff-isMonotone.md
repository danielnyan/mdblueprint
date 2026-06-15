---
id: isImplementable-iff-isMonotone
title: isImplementable_iff_isMonotone
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - isImplementable_iff_isMonotone
uses:
  - IsImplementable
  - IsMonotone
  - isMonotone_of_isDSIC
  - isImplementable_of_isMonotone
---

# isImplementable_iff_isMonotone

## Lean type

```lean
theorem isImplementable_iff_isMonotone [DecidableEq I] (x : (I → ℝ) → I → ℝ) : IsImplementable x ↔ IsMonotone ({ allocationRule
```

## Dependencies

- IsImplementable
- IsMonotone
- isMonotone_of_isDSIC
- isImplementable_of_isMonotone
