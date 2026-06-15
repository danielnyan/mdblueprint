---
id: equilibriumPayoff-eq-neg-interimExpectedPayment-zero-add-integral
title: equilibriumPayoff_eq_neg_interimExpectedPayment_zero_add_integral
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - equilibriumPayoff_eq_neg_interimExpectedPayment_zero_add_integral
uses:
  - HasInterimEnvelopeFormula
---

# equilibriumPayoff_eq_neg_interimExpectedPayment_zero_add_integral

## Lean type

```lean
theorem equilibriumPayoff_eq_neg_interimExpectedPayment_zero_add_integral (A : BayesianSingleItemAuction I) (henv : A.HasInterimEnvelopeFormula) (i : I) (v_i : ℝ) : A.equilibriumPayoff i v_i = -A.interimExpectedPayment i 0 + ∫ z in 0..v_i, A.interimAllocProb i z
```

## Dependencies

- HasInterimEnvelopeFormula
