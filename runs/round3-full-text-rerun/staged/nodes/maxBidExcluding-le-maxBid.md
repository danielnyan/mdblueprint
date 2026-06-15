---
id: maxBidExcluding-le-maxBid
title: maxBidExcluding_le_maxBid
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.AuctionBasic
  declarations:
    - maxBidExcluding_le_maxBid
uses:
  - maxBid
---

# maxBidExcluding_le_maxBid

## Lean type

```lean
lemma maxBidExcluding_le_maxBid (i : I) : maxBidExcluding b i ≤ maxBid b
```

## Dependencies

- maxBid
