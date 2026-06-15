---
id: index-split-spec
title: index_split_spec
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - index_split_spec
uses:
  - index_split_existence
  - Profile.ext
---

# index_split_spec

## Lean type

```lean
lemma index_split_spec (k : Fin (total_card card)) : let p
```

## Dependencies

- index_split_existence
- Profile.ext
