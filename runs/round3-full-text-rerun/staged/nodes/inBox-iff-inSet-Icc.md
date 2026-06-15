---
id: inBox-iff-inSet-Icc
title: inBox_iff_inSet_Icc
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.AuctionBasic
  declarations:
    - inBox_iff_inSet_Icc
uses:
  - InBox
  - InSet
---

# inBox_iff_inSet_Icc

## Lean type

```lean
lemma inBox_iff_inSet_Icc [Preorder V] (b : I → V) (ℓ u : I → V) : InBox b ℓ u ↔ InSet b (fun i => Set.Icc (ℓ i) (u i))
```

## Dependencies

- InBox
- InSet
