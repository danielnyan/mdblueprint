---
id: maxBidExcluding-eq-maxBid-of-not-argmax
title: maxBidExcluding_eq_maxBid_of_not_argmax
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.AuctionBasic
  declarations:
    - maxBidExcluding_eq_maxBid_of_not_argmax
uses:
  - maxBid
  - maxBidExcluding_le_maxBid
  - argmaxBid_eq_maxBid
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# maxBidExcluding_eq_maxBid_of_not_argmax

## Lean type

```lean
lemma maxBidExcluding_eq_maxBid_of_not_argmax {i : I} (h : i ≠ argmaxBid b) : maxBidExcluding b i = maxBid b
```

## Dependencies

- maxBid
- maxBidExcluding_le_maxBid
- argmaxBid_eq_maxBid
- IsPositiveAffineOf.symm
- Indifferent.symm
