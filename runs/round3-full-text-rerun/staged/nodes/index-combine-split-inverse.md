---
id: index-combine-split-inverse
title: index_combine_split_inverse
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - index_combine_split_inverse
uses:
  - index_split_spec
  - Profile.ext
  - BigSimplex
  - ProductSimplices
  - Pos
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - index_split_combine_inverse
---

# index_combine_split_inverse

## Lean type

```lean
lemma index_combine_split_inverse (k : Fin (total_card card)) : index_combine card (index_split card k) = k
```

## Dependencies

- index_split_spec
- Profile.ext
- BigSimplex
- ProductSimplices
- Pos
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
- IsPositiveAffineOf.symm
- Indifferent.symm
- index_split_combine_inverse
