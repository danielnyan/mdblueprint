---
id: IsDSIC
title: IsDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Transfer
  declarations:
    - IsDSIC
uses:
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - toStrategicGame
  - isDSIC
---

# IsDSIC

## Lean type

```lean
def IsDSIC [Mul R] [Sub R] [Preorder R] : Prop
```

## Dependencies

- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- toStrategicGame
- isDSIC
