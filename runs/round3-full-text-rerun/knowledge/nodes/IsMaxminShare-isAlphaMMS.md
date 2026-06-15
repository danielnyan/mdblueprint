---
id: IsMaxminShare-isAlphaMMS
title: IsMaxminShare.isAlphaMMS
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.MMS
  declarations:
    - IsMaxminShare.isAlphaMMS
uses:
  - Valuation
  - Allocation
  - IsProportional.isMaxminShare
  - IsMaxminShare
  - IsAlphaMMS
  - isAlphaMMS_mono_alpha
  - isMaxminShare_iff_isAlphaMMS_one
---

# IsMaxminShare.isAlphaMMS

## Lean type

```lean
theorem IsMaxminShare.isAlphaMMS [Nonempty N] [Fintype G] (v : Valuation N G) (allGoods : Finset G) (A : Allocation N G) (hne : Nonempty {A' : Allocation N G // IsAllocation allGoods A'}) (hMMS : IsMaxminShare v allGoods A) (α : ℝ) (hα_le : α ≤ 1) (hmms_nn : ∀ i, 0 ≤ mmsValue v allGoods i) : IsAlphaMMS α v allGoods A
```

## Dependencies

- Valuation
- Allocation
- IsProportional.isMaxminShare
- IsMaxminShare
- IsAlphaMMS
- isAlphaMMS_mono_alpha
- isMaxminShare_iff_isAlphaMMS_one
