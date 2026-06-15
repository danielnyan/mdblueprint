---
id: IsZeroNormalized
title: IsZeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsZeroNormalized
uses:
  - ZeroNormalized
---

# IsZeroNormalized

## Lean type

```lean
def IsZeroNormalized [DecidableEq I] (B : BayesianSingleItemAuction I) : Prop
```

## Dependencies

- ZeroNormalized
