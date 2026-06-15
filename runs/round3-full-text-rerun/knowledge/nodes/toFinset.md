---
id: toFinset
title: toFinset
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.AuctionBasic
  declarations:
    - toFinset
uses:
  - Visited
  - MultiItemBundle
---

# toFinset

## Lean type

```lean
def toFinset {k : ℕ} (bundle : MultiItemBundle k) : Finset (Fin k)
```

## Dependencies

- Visited
- MultiItemBundle
