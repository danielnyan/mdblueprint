---
id: bid-le-maxBid
title: bid_le_maxBid
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.AuctionBasic
  declarations:
    - bid_le_maxBid
uses:
  - argmaxBid_eq_maxBid
---

# bid_le_maxBid

## Lean type

```lean
lemma bid_le_maxBid (j : I) : b j ≤ b (argmaxBid b)
```

## Dependencies

- argmaxBid_eq_maxBid
