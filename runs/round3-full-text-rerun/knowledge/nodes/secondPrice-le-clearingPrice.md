---
id: secondPrice-le-clearingPrice
title: secondPrice_le_clearingPrice
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - secondPrice_le_clearingPrice
uses:
  - Allocation
---

# secondPrice_le_clearingPrice

## Lean type

```lean
lemma secondPrice_le_clearingPrice (reserve : U) (b : I → U) : SecondPrice.secondPrice b ≤ clearingPrice reserve b
```

## Dependencies

- Allocation
