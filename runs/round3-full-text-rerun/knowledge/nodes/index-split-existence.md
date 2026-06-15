---
id: index-split-existence
title: index_split_existence
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer_product
  declarations:
    - index_split_existence
uses:
  - Profile.ext
---

# index_split_existence

## Lean type

```lean
lemma index_split_existence (k : Fin (total_card card)) : ∃ (p : Σ i, Fin (card i)), prefix_sum card p.1 ≤ k.val ∧ k.val < prefix_sum card p.1 + (card p.1 : ℕ) ∧ p.2.val = k.val - prefix_sum card p.1
```

## Dependencies

- Profile.ext
