---
id: Brouwer-Product
title: Brouwer_Product
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - Brouwer_Product
uses:
  - ProductSimplices
  - colRatio.continuous
  - lamB.aux.continuous
  - rowRatio.continuous
  - lam.aux.continuous
  - muB.aux.continuous
  - mu.aux.continuous
  - BigSimplex
  - embed_continuous
  - project_continuous
  - Brouwer
  - project_embed_id
---

# Brouwer_Product

## Lean type

```lean
theorem Brouwer_Product (f : ProductSimplices card → ProductSimplices card) (hf : Continuous f) : ∃ x : ProductSimplices card, f x = x
```

## Dependencies

- ProductSimplices
- colRatio.continuous
- lamB.aux.continuous
- rowRatio.continuous
- lam.aux.continuous
- muB.aux.continuous
- mu.aux.continuous
- BigSimplex
- embed_continuous
- project_continuous
- Brouwer
- project_embed_id
