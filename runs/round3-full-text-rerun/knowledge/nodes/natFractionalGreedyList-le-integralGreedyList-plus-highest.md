---
id: natFractionalGreedyList-le-integralGreedyList-plus-highest
title: natFractionalGreedyList_le_integralGreedyList_plus_highest
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.Knapsack
  declarations:
    - natFractionalGreedyList_le_integralGreedyList_plus_highest
uses:
  - fractionalSocialWelfare
  - realBidOfNat
  - natBinarySocialWelfare
  - integralGreedyList
  - eq_zero_of_fractionalSupportedOn_of_not_mem
  - natFractionalGreedyList_supportedOn
  - eq_false_of_supportedOn_of_not_mem
  - integralGreedyList_supportedOn
  - natBinarySocialWelfare_update_true_of_false
  - fractionalSocialWelfare_update_one_of_zero
  - fractionalSocialWelfare_singleton
  - le_highestBidValue
---

# natFractionalGreedyList_le_integralGreedyList_plus_highest

## Lean type

```lean
lemma natFractionalGreedyList_le_integralGreedyList_plus_highest (w b : I → Nat) (hwpos : ∀ i, 0 < w i) : ∀ {items : List I}, items.Nodup → ∀ remaining, fractionalSocialWelfare (realBidOfNat b) (natFractionalGreedyList w items remaining) ≤ (natBinarySocialWelfare b (integralGreedyList w items remaining) : ℝ) + highestBidValue b
```

## Dependencies

- fractionalSocialWelfare
- realBidOfNat
- natBinarySocialWelfare
- integralGreedyList
- eq_zero_of_fractionalSupportedOn_of_not_mem
- natFractionalGreedyList_supportedOn
- eq_false_of_supportedOn_of_not_mem
- integralGreedyList_supportedOn
- natBinarySocialWelfare_update_true_of_false
- fractionalSocialWelfare_update_one_of_zero
- fractionalSocialWelfare_singleton
- le_highestBidValue
