---
id: maxBidExcluding-le-argmaxBid-bid
title: maxBidExcluding_le_argmaxBid_bid
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.AuctionBasic
  declarations:
    - maxBidExcluding_le_argmaxBid_bid
uses:
  - maxBid
  - maxBidExcluding_le_maxBid
  - argmaxBid_eq_maxBid
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# maxBidExcluding_le_argmaxBid_bid

## Lean type

```lean
lemma maxBidExcluding_le_argmaxBid_bid : maxBidExcluding b (argmaxBid b) ≤ b (argmaxBid b)
```

## Dependencies

- maxBid
- maxBidExcluding_le_maxBid
- argmaxBid_eq_maxBid
- IsPositiveAffineOf.symm
- Indifferent.symm
