---
id: isQuasiLinearDSIC
title: isQuasiLinearDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Transfer
  declarations:
    - isQuasiLinearDSIC
uses:
  - IsDSIC
  - isDSIC
---

# isQuasiLinearDSIC

## Lean type

```lean
def isQuasiLinearDSIC [Sub U] [Preorder U] (val : A → (∀ i, T i) → I → V) (valueToUtility : V → U) (paymentToUtility : P → U) : Prop
```

## Dependencies

- IsDSIC
- isDSIC
