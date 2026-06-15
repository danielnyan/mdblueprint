---
id: reserve-le-clearingPrice
title: reserve_le_clearingPrice
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - reserve_le_clearingPrice
uses:
---

# reserve_le_clearingPrice

## Lean type

```lean
lemma reserve_le_clearingPrice (reserve : U) (b : I → U) : reserve ≤ clearingPrice reserve b
```

## Dependencies

- none
