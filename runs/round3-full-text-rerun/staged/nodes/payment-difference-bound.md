---
id: payment-difference-bound
title: payment_difference_bound
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - payment_difference_bound
uses:
  - IsDSIC
  - isDSIC
  - payment_sandwich
---

# payment_difference_bound

## Lean type

```lean
theorem payment_difference_bound [DecidableEq I] {x p q : (I → ℝ) → I → ℝ} (hpdsic : ({ allocationRule
```

## Dependencies

- IsDSIC
- isDSIC
- payment_sandwich
