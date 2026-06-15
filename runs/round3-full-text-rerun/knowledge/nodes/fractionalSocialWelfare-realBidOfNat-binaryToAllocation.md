---
id: fractionalSocialWelfare-realBidOfNat-binaryToAllocation
title: fractionalSocialWelfare_realBidOfNat_binaryToAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - fractionalSocialWelfare_realBidOfNat_binaryToAllocation
uses:
  - BinaryAllocation
  - fractionalSocialWelfare
  - realBidOfNat
  - binaryToAllocation
  - natBinarySocialWelfare
  - natAuctionData
---

# fractionalSocialWelfare_realBidOfNat_binaryToAllocation

## Lean type

```lean
lemma fractionalSocialWelfare_realBidOfNat_binaryToAllocation (b : I → Nat) (x : BinaryAllocation I) : fractionalSocialWelfare (realBidOfNat b) (binaryToAllocation x) = natBinarySocialWelfare b x
```

## Dependencies

- BinaryAllocation
- fractionalSocialWelfare
- realBidOfNat
- binaryToAllocation
- natBinarySocialWelfare
- natAuctionData
