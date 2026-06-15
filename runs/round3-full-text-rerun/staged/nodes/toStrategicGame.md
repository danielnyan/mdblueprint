---
id: toStrategicGame
title: toStrategicGame
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Transfer
  declarations:
    - toStrategicGame
uses:
  - Strategy
  - Strategy
---

# toStrategicGame

## Lean type

```lean
def toStrategicGame (u : A → (I → P) → (∀ i, T i) → I → U) (trueTypes : ∀ i, T i) : StrategicGame I U
```

## Dependencies

- Strategy
- Strategy
