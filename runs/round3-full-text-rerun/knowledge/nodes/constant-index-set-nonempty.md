---
id: constant-index-set-nonempty
title: constant_index_set_nonempty
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - constant_index_set_nonempty
uses:
  - room_seq
  - exists_subseq_constant_of_finite_image
---

# constant_index_set_nonempty

## Lean type

```lean
lemma constant_index_set_nonempty : Nonempty {(a, g) :(Finset (Fin n)) × (ℕ ↪o ℕ) | ∀ l', (room_seq f (g l')).1.2 = a }
```

## Dependencies

- room_seq
- exists_subseq_constant_of_finite_image
