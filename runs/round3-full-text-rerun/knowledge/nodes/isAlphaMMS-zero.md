---
id: isAlphaMMS-zero
title: isAlphaMMS_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.MMS
  declarations:
    - isAlphaMMS_zero
uses:
  - Valuation
  - Allocation
  - IsMaxminShare.isAlphaMMS
  - IsAlphaMMS
---

# isAlphaMMS_zero

## Lean type

```lean
theorem isAlphaMMS_zero (v : Valuation N G) (allGoods : Finset G) (A : Allocation N G) (hnonneg : ∀ i S, 0 ≤ v.val i S) : IsAlphaMMS 0 v allGoods A
```

## Dependencies

- Valuation
- Allocation
- IsMaxminShare.isAlphaMMS
- IsAlphaMMS
