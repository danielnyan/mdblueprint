---
id: payment-formula-of-isDSIC-of-zeroNormalized
title: payment_formula_of_isDSIC_of_zeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - payment_formula_of_isDSIC_of_zeroNormalized
uses:
  - IsDSIC
  - isDSIC
  - ZeroNormalized
  - IsMonotone
  - isMonotone_of_isDSIC
  - withMyersonPayment_isDSIC_of_isMonotone
  - payment_difference_bound
  - myersonPayment_zeroNormalized
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# payment_formula_of_isDSIC_of_zeroNormalized

## Lean type

```lean
theorem payment_formula_of_isDSIC_of_zeroNormalized [DecidableEq I] {x p : (I → ℝ) → I → ℝ} (hdsic : ({ allocationRule
```

## Dependencies

- IsDSIC
- isDSIC
- ZeroNormalized
- IsMonotone
- isMonotone_of_isDSIC
- withMyersonPayment_isDSIC_of_isMonotone
- payment_difference_bound
- myersonPayment_zeroNormalized
- IsPositiveAffineOf.symm
- Indifferent.symm
