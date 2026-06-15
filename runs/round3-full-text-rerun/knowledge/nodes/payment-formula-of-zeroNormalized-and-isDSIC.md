---
id: payment-formula-of-zeroNormalized-and-isDSIC
title: payment_formula_of_zeroNormalized_and_isDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - payment_formula_of_zeroNormalized_and_isDSIC
uses:
  - ZeroNormalized
  - IsDSIC
  - isDSIC
  - payment_formula_of_isDSIC_of_zeroNormalized
---

# payment_formula_of_zeroNormalized_and_isDSIC

## Lean type

```lean
theorem payment_formula_of_zeroNormalized_and_isDSIC [DecidableEq I] {x p : (I → ℝ) → I → ℝ} (hp : ZeroNormalized p ∧ ({ allocationRule
```

## Dependencies

- ZeroNormalized
- IsDSIC
- isDSIC
- payment_formula_of_isDSIC_of_zeroNormalized
