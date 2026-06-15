---
id: quasiLinearUtility-eq-transferQuasiLinearUtility
title: quasiLinearUtility_eq_transferQuasiLinearUtility
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Transfer
  declarations:
    - quasiLinearUtility_eq_transferQuasiLinearUtility
uses:
  - quasiLinearUtility
---

# quasiLinearUtility_eq_transferQuasiLinearUtility

## Lean type

```lean
lemma quasiLinearUtility_eq_transferQuasiLinearUtility [Mul R] [Sub R] (b θ : I → R) (i : I) : M.quasiLinearUtility b θ i = MechanismWithTransfers.quasiLinearUtility (I
```

## Dependencies

- quasiLinearUtility
