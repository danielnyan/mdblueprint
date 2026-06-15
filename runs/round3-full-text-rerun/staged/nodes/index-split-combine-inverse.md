---
id: index-split-combine-inverse
title: index_split_combine_inverse
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - index_split_combine_inverse
uses:
  - index_split_spec
  - Profile.ext
---

# index_split_combine_inverse

## Lean type

```lean
lemma index_split_combine_inverse (p : Σ i, Fin (card i)) : index_split card (index_combine card p) = p
```

## Dependencies

- index_split_spec
- Profile.ext
