---
id: maxBidExcluding-update-self
title: maxBidExcluding_update_self
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.AuctionBasic
  declarations:
    - maxBidExcluding_update_self
uses:
---

# maxBidExcluding_update_self

## Lean type

```lean
lemma maxBidExcluding_update_self (i : I) (bi : V) : maxBidExcluding (Function.update b i bi) i = maxBidExcluding b i
```

## Dependencies

- none
