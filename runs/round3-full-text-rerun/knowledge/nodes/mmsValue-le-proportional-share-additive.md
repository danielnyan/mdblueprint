---
id: mmsValue-le-proportional-share-additive
title: mmsValue_le_proportional_share_additive
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.MMS
  declarations:
    - mmsValue_le_proportional_share_additive
uses:
  - Allocation
  - toValuation
  - mmsValue_le_of_forall
---

# mmsValue_le_proportional_share_additive

## Lean type

```lean
lemma mmsValue_le_proportional_share_additive (w : AdditiveValuation N G) (allGoods : Finset G) (i : N) (hne : Nonempty {A : Allocation N G // IsAllocation allGoods A}) : (Fintype.card N : ℝ) * mmsValue w.toValuation allGoods i ≤ w.toValuation.val i allGoods
```

## Dependencies

- Allocation
- toValuation
- mmsValue_le_of_forall
