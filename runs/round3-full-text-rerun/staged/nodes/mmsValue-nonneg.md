---
id: mmsValue-nonneg
title: mmsValue_nonneg
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.MMS
  declarations:
    - mmsValue_nonneg
uses:
  - Valuation
  - Allocation
---

# mmsValue_nonneg

## Lean type

```lean
lemma mmsValue_nonneg [Fintype G] (v : Valuation N G) (allGoods : Finset G) (i : N) (hne : Nonempty {A : Allocation N G // IsAllocation allGoods A}) (hnonneg : ∀ S : Finset G, 0 ≤ v.val i S) : 0 ≤ mmsValue v allGoods i
```

## Dependencies

- Valuation
- Allocation
