---
id: reserve-le-bid-winner-of-allocation-eq-some
title: reserve_le_bid_winner_of_allocation_eq_some
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - reserve_le_bid_winner_of_allocation_eq_some
uses:
  - Allocation
---

# reserve_le_bid_winner_of_allocation_eq_some

## Lean type

```lean
lemma reserve_le_bid_winner_of_allocation_eq_some {reserve : U} {b : I → U} {i : I} (halloc : allocation reserve b = some i) : reserve ≤ b (SecondPrice.winner b)
```

## Dependencies

- Allocation
