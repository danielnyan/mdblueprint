---
id: withMyersonPayment-quasiLinearUtility-eq
title: withMyersonPayment_quasiLinearUtility_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - withMyersonPayment_quasiLinearUtility_eq
uses:
  - quasiLinearUtility
  - quasiLinearValue
---

# withMyersonPayment_quasiLinearUtility_eq

## Lean type

```lean
lemma withMyersonPayment_quasiLinearUtility_eq [DecidableEq I] (x : (I → ℝ) → I → ℝ) (v b : I → ℝ) (i : I) : (withMyersonPayment x).quasiLinearUtility b v i = (v i - b i) * x b i + ∫ z in 0..b i, x (Function.update b i z) i
```

## Dependencies

- quasiLinearUtility
- quasiLinearValue
