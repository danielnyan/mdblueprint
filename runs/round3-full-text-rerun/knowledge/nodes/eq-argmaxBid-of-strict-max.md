---
id: eq-argmaxBid-of-strict-max
title: eq_argmaxBid_of_strict_max
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.AuctionBasic
  declarations:
    - eq_argmaxBid_of_strict_max
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - bid_le_maxBid
---

# eq_argmaxBid_of_strict_max

## Lean type

```lean
lemma eq_argmaxBid_of_strict_max (i : I) (h : ∀ j, j ≠ i → b j < b i) : i = argmaxBid b
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
- bid_le_maxBid
