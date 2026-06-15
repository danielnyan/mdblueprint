---
id: utility-nonneg
title: utility_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Vickrey
  declarations:
    - utility_nonneg
uses:
  - Allocation
  - utility_winner
  - clearingPrice_le_bid_of_allocation_eq_some
  - utility_loser
  - utility_winner
  - secondPrice_le_bid_winner
  - utility_loser
---

# utility_nonneg

## Lean type

```lean
lemma utility_nonneg {b : I → U} {i : I} (htruth : b i = v i) : 0 ≤ utility v b i
```

## Dependencies

- Allocation
- utility_winner
- clearingPrice_le_bid_of_allocation_eq_some
- utility_loser
- utility_winner
- secondPrice_le_bid_winner
- utility_loser
