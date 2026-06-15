---
id: isMaxminShare-iff-isAlphaMMS-one
title: isMaxminShare_iff_isAlphaMMS_one
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.MMS
  declarations:
    - isMaxminShare_iff_isAlphaMMS_one
uses:
  - Valuation
  - Allocation
  - IsProportional.isMaxminShare
  - IsMaxminShare
  - IsMaxminShare.isAlphaMMS
  - IsAlphaMMS
---

# isMaxminShare_iff_isAlphaMMS_one

## Lean type

```lean
theorem isMaxminShare_iff_isAlphaMMS_one [Nonempty N] [Fintype G] (v : Valuation N G) (allGoods : Finset G) (A : Allocation N G) (hne : Nonempty {A' : Allocation N G // IsAllocation allGoods A'}) : IsMaxminShare v allGoods A ↔ IsAlphaMMS 1 v allGoods A
```

## Dependencies

- Valuation
- Allocation
- IsProportional.isMaxminShare
- IsMaxminShare
- IsMaxminShare.isAlphaMMS
- IsAlphaMMS
