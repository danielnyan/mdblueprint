---
id: project-embed-id
title: project_embed_id
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - project_embed_id
uses:
  - ProductSimplices
  - index_split_combine_inverse
  - Profile.ext
  - Pos
---

# project_embed_id

## Lean type

```lean
lemma project_embed_id (y : ProductSimplices card) : project_to_product card (embed_from_product card y) = y
```

## Dependencies

- ProductSimplices
- index_split_combine_inverse
- Profile.ext
- Pos
