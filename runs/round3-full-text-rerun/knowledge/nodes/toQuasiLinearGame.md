---
id: toQuasiLinearGame
title: toQuasiLinearGame
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Transfer
  declarations:
    - toQuasiLinearGame
uses:
  - toStrategicGame
---

# toQuasiLinearGame

## Lean type

```lean
def toQuasiLinearGame [Sub U] (val : A → (∀ i, T i) → I → V) (valueToUtility : V → U) (paymentToUtility : P → U) (trueTypes : ∀ i, T i) : StrategicGame I U
```

## Dependencies

- toStrategicGame
