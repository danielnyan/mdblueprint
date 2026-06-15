---
id: winner-eq-of-allocation-eq-some
title: winner_eq_of_allocation_eq_some
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - winner_eq_of_allocation_eq_some
uses:
  - Allocation
---

# winner_eq_of_allocation_eq_some

## Lean type

```lean
lemma winner_eq_of_allocation_eq_some {reserve : U} {b : I → U} {i : I} (halloc : allocation reserve b = some i) : SecondPrice.winner b = i
```

## Dependencies

- Allocation
