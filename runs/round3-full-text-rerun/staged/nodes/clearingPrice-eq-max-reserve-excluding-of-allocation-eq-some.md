---
id: clearingPrice-eq-max-reserve-excluding-of-allocation-eq-some
title: clearingPrice_eq_max_reserve_excluding_of_allocation_eq_some
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.ReserveVickrey
  declarations:
    - clearingPrice_eq_max_reserve_excluding_of_allocation_eq_some
uses:
  - Allocation
  - winner_eq_of_allocation_eq_some
  - bid_le_maxBid
  - maxBid
  - maxBidExcluding_eq_maxBid_of_not_argmax
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - argmaxBid_eq_maxBid
  - maxBidExcluding_update_self
---

# clearingPrice_eq_max_reserve_excluding_of_allocation_eq_some

## Lean type

```lean
lemma clearingPrice_eq_max_reserve_excluding_of_allocation_eq_some {reserve : U} {b : I → U} {i : I} (halloc : allocation reserve b = some i) : clearingPrice reserve b = max reserve (Auction.maxBidExcluding b i)
```

## Dependencies

- Allocation
- winner_eq_of_allocation_eq_some
- bid_le_maxBid
- maxBid
- maxBidExcluding_eq_maxBid_of_not_argmax
- IsPositiveAffineOf.symm
- Indifferent.symm
- argmaxBid_eq_maxBid
- maxBidExcluding_update_self
