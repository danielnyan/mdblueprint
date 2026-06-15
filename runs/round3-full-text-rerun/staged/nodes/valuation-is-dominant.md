---
id: valuation-is-dominant
title: valuation_is_dominant
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Vickrey
  declarations:
    - valuation_is_dominant
uses:
  - Allocation
  - utility_winner
  - clearingPrice_eq_max_reserve_excluding_of_allocation_eq_some
  - maxBidExcluding_update_self
  - utility_loser
  - utility_nonneg
  - Strategy
  - maxBidExcluding_update_self
  - utility_winner
  - utility_loser
  - utility_nonneg
  - Strategy
---

# valuation_is_dominant

## Lean type

```lean
theorem valuation_is_dominant (v : I → U) (i : I) (b : I → U) : utility v b i ≤ utility v (Function.update b i (v i)) i
```

## Dependencies

- Allocation
- utility_winner
- clearingPrice_eq_max_reserve_excluding_of_allocation_eq_some
- maxBidExcluding_update_self
- utility_loser
- utility_nonneg
- Strategy
- maxBidExcluding_update_self
- utility_winner
- utility_loser
- utility_nonneg
- Strategy
