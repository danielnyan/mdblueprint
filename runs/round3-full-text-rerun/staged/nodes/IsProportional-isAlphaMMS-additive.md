---
id: IsProportional-isAlphaMMS-additive
title: IsProportional.isAlphaMMS_additive
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.MMS
  declarations:
    - IsProportional.isAlphaMMS_additive
uses:
  - Allocation
  - IsEnvyFree.isProportional
  - IsProportional
  - toValuation
  - IsMaxminShare.isAlphaMMS
  - IsAlphaMMS
  - IsProportional.isMaxminShare
  - IsMaxminShare
---

# IsProportional.isAlphaMMS_additive

## Lean type

```lean
theorem IsProportional.isAlphaMMS_additive [Nonempty N] [Fintype G] (w : AdditiveValuation N G) {allGoods : Finset G} {A : Allocation N G} (hne : Nonempty {A' : Allocation N G // IsAllocation allGoods A'}) (hProp : IsProportional (Fintype.card N) w.toValuation allGoods A) (α : ℝ) (hα_le : α ≤ 1) (hmms_nn : ∀ i, 0 ≤ mmsValue w.toValuation allGoods i) : IsAlphaMMS α w.toValuation allGoods A
```

## Dependencies

- Allocation
- IsEnvyFree.isProportional
- IsProportional
- toValuation
- IsMaxminShare.isAlphaMMS
- IsAlphaMMS
- IsProportional.isMaxminShare
- IsMaxminShare
