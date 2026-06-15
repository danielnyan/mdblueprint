---
id: IsImplementable
title: IsImplementable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Transfer
  declarations:
    - IsImplementable
uses:
  - IsDSIC
  - isDSIC
---

# IsImplementable

## Lean type

```lean
def IsImplementable [Mul R] [Sub R] [Preorder R] (x : (I → R) → I → R) : Prop
```

## Dependencies

- IsDSIC
- isDSIC
