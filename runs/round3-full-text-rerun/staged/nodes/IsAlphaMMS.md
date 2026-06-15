---
id: IsAlphaMMS
title: IsAlphaMMS
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.MMS
  declarations:
    - IsAlphaMMS
uses:
  - Valuation
  - Allocation
---

# IsAlphaMMS

## Lean type

```lean
def IsAlphaMMS [Fintype N] [DecidableEq G] (α : ℝ) (v : Valuation N G) (allGoods : Finset G) (A : Allocation N G) : Prop
```

## Dependencies

- Valuation
- Allocation
