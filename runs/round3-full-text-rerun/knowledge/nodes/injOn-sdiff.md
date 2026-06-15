---
id: injOn-sdiff
title: injOn_sdiff
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - injOn_sdiff
uses:
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - Profile.ext
---

# injOn_sdiff

## Lean type

```lean
lemma injOn_sdiff (s : Finset X) (f : X → Y) (h : s.card = (Finset.image f s).card + 1) : ∃ a b, a ∈ s ∧ b ∈ s ∧ f a = f b ∧ a ≠ b ∧ Set.InjOn f (s \ ({a, b} : Finset X))
```

## Dependencies

- IsPositiveAffineOf.symm
- Indifferent.symm
- Profile.ext
