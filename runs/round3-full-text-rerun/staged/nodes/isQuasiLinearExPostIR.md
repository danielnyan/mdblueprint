---
id: isQuasiLinearExPostIR
title: isQuasiLinearExPostIR
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Transfer
  declarations:
    - isQuasiLinearExPostIR
uses:
  - IsExPostIR
  - isExPostIR
---

# isQuasiLinearExPostIR

## Lean type

```lean
def isQuasiLinearExPostIR [Sub U] [Preorder U] [Zero U] (val : A → (∀ i, T i) → I → V) (valueToUtility : V → U) (paymentToUtility : P → U) : Prop
```

## Dependencies

- IsExPostIR
- isExPostIR
