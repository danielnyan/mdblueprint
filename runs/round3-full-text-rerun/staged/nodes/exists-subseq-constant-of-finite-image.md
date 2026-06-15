---
id: exists-subseq-constant-of-finite-image
title: exists_subseq_constant_of_finite_image
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Brouwer
  declarations:
    - exists_subseq_constant_of_finite_image
uses:
  - Profile.ext
  - mk_subseq
---

# exists_subseq_constant_of_finite_image

## Lean type

```lean
theorem exists_subseq_constant_of_finite_image {s : Finset X} (e : ℕ → X) (he : ∀ n, e n ∈ s ) : ∃ a ∈ s, ∃ g : ℕ ↪o ℕ, (∀ n, e (g n) = a)
```

## Dependencies

- Profile.ext
- mk_subseq
