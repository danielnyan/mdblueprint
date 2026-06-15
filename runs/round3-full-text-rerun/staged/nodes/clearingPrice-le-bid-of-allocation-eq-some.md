---
id: clearingPrice-le-bid-of-allocation-eq-some
title: clearingPrice_le_bid_of_allocation_eq_some
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - clearingPrice_le_bid_of_allocation_eq_some
uses:
  - Allocation
  - winner_eq_of_allocation_eq_some
  - reserve_le_bid_winner_of_allocation_eq_some
  - secondPrice_le_bid_winner
---

# clearingPrice_le_bid_of_allocation_eq_some

## Lean type

```lean
lemma clearingPrice_le_bid_of_allocation_eq_some {reserve : U} {b : I → U} {i : I} (halloc : allocation reserve b = some i) : clearingPrice reserve b ≤ b i
```

## Dependencies

- Allocation
- winner_eq_of_allocation_eq_some
- reserve_le_bid_winner_of_allocation_eq_some
- secondPrice_le_bid_winner
