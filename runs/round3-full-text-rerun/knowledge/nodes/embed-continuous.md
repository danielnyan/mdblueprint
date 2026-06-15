---
id: embed-continuous
title: embed_continuous
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - embed_continuous
uses:
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - ProductSimplices
  - Pos
---

# embed_continuous

## Lean type

```lean
lemma embed_continuous : Continuous (embed_from_product card)
```

## Dependencies

- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- ProductSimplices
- Pos
