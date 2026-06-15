---
id: argmaxBid-eq-maxBid
title: argmaxBid_eq_maxBid
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.AuctionBasic
  declarations:
    - argmaxBid_eq_maxBid
uses:
  - maxBid
  - exists_maxBid
---

# argmaxBid_eq_maxBid

## Lean type

```lean
lemma argmaxBid_eq_maxBid : b (argmaxBid b) = maxBid b
```

## Dependencies

- maxBid
- exists_maxBid
