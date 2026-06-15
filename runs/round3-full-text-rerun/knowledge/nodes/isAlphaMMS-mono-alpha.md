---
id: isAlphaMMS-mono-alpha
title: isAlphaMMS_mono_alpha
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.MMS
  declarations:
    - isAlphaMMS_mono_alpha
uses:
  - Valuation
  - Allocation
  - IsMaxminShare.isAlphaMMS
  - IsAlphaMMS
---

# isAlphaMMS_mono_alpha

## Lean type

```lean
theorem isAlphaMMS_mono_alpha (v : Valuation N G) (allGoods : Finset G) (A : Allocation N G) (α β : ℝ) (hβα : β ≤ α) (hmms_nn : ∀ i, 0 ≤ mmsValue v allGoods i) (hα : IsAlphaMMS α v allGoods A) : IsAlphaMMS β v allGoods A
```

## Dependencies

- Valuation
- Allocation
- IsMaxminShare.isAlphaMMS
- IsAlphaMMS
