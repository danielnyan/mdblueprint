---
id: secondPrice-le-bid-winner
title: secondPrice_le_bid_winner
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Vickrey
  declarations:
    - secondPrice_le_bid_winner
uses:
  - maxBid
  - maxBidExcluding_le_maxBid
  - argmaxBid_eq_maxBid
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# secondPrice_le_bid_winner

## Lean type

```lean
lemma secondPrice_le_bid_winner (b : I → U) : secondPrice b ≤ b (winner b)
```

## Dependencies

- maxBid
- maxBidExcluding_le_maxBid
- argmaxBid_eq_maxBid
- IsPositiveAffineOf.symm
- Indifferent.symm
