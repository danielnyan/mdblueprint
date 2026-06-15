---
id: isDSIC
title: isDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Transfer
  declarations:
    - isDSIC
uses:
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - toStrategicGame
---

# isDSIC

## Lean type

```lean
def isDSIC [Preorder U] (u : A → (I → P) → (∀ i, T i) → I → U) : Prop
```

## Dependencies

- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- toStrategicGame
