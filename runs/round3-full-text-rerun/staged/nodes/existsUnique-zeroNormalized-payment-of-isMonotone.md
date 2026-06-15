---
id: existsUnique-zeroNormalized-payment-of-isMonotone
title: existsUnique_zeroNormalized_payment_of_isMonotone
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - existsUnique_zeroNormalized_payment_of_isMonotone
uses:
  - IsMonotone
  - ZeroNormalized
  - IsDSIC
  - isDSIC
  - myersonPayment_zeroNormalized
  - withMyersonPayment_isDSIC_of_isMonotone
  - payment_eq_myersonPayment_of_isDSIC_of_zeroNormalized
---

# existsUnique_zeroNormalized_payment_of_isMonotone

## Lean type

```lean
theorem existsUnique_zeroNormalized_payment_of_isMonotone [DecidableEq I] {x : (I → ℝ) → I → ℝ} (hx : IsMonotone ({ allocationRule
```

## Dependencies

- IsMonotone
- ZeroNormalized
- IsDSIC
- isDSIC
- myersonPayment_zeroNormalized
- withMyersonPayment_isDSIC_of_isMonotone
- payment_eq_myersonPayment_of_isDSIC_of_zeroNormalized
