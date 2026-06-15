---
id: exists-maxBid
title: exists_maxBid
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.AuctionBasic
  declarations:
    - exists_maxBid
uses:
  - maxBid
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# exists_maxBid

## Lean type

```lean
lemma exists_maxBid : ∃ i : I, b i = maxBid b
```

## Dependencies

- maxBid
- IsPositiveAffineOf.symm
- Indifferent.symm
