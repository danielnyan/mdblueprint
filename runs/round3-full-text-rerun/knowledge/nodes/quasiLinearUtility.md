---
id: quasiLinearUtility
title: quasiLinearUtility
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Transfer
  declarations:
    - quasiLinearUtility
uses:
  - quasiLinearValue
---

# quasiLinearUtility

## Lean type

```lean
def quasiLinearUtility [Mul R] [Sub R] (b θ : I → R) (i : I) : R
```

## Dependencies

- quasiLinearValue
