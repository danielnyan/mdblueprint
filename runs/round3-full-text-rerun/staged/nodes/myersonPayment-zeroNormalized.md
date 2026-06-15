---
id: myersonPayment-zeroNormalized
title: myersonPayment_zeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Myerson
  declarations:
    - myersonPayment_zeroNormalized
uses:
  - ZeroNormalized
---

# myersonPayment_zeroNormalized

## Lean type

```lean
theorem myersonPayment_zeroNormalized [DecidableEq I] (x : (I → ℝ) → I → ℝ) : ZeroNormalized (myersonPayment x)
```

## Dependencies

- ZeroNormalized
