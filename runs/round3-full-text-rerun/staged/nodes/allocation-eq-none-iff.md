---
id: allocation-eq-none-iff
title: allocation_eq_none_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - allocation_eq_none_iff
uses:
  - Allocation
---

# allocation_eq_none_iff

## Lean type

```lean
lemma allocation_eq_none_iff {reserve : U} {b : I → U} : allocation reserve b = none ↔ b (SecondPrice.winner b) < reserve
```

## Dependencies

- Allocation
