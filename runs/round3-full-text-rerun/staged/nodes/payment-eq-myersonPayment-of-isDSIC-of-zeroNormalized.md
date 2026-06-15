---
id: payment-eq-myersonPayment-of-isDSIC-of-zeroNormalized
title: payment_eq_myersonPayment_of_isDSIC_of_zeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - payment_eq_myersonPayment_of_isDSIC_of_zeroNormalized
uses:
  - IsDSIC
  - isDSIC
  - ZeroNormalized
  - payment_formula_of_isDSIC_of_zeroNormalized
---

# payment_eq_myersonPayment_of_isDSIC_of_zeroNormalized

## Lean type

```lean
theorem payment_eq_myersonPayment_of_isDSIC_of_zeroNormalized [DecidableEq I] {x p : (I → ℝ) → I → ℝ} (hdsic : ({ allocationRule
```

## Dependencies

- IsDSIC
- isDSIC
- ZeroNormalized
- payment_formula_of_isDSIC_of_zeroNormalized
