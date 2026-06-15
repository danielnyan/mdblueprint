---
id: image-erase-collision-preserves
title: image_erase_collision_preserves
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - image_erase_collision_preserves
uses:
  - Profile.ext
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# image_erase_collision_preserves

## Lean type

```lean
lemma image_erase_collision_preserves [DecidableEq T] (σ : Finset T) (c : T → I) (x y : T) (hx_in_σ : x ∈ σ) (hy_in_σ : y ∈ σ) (hxy_ne : x ≠ y) (hcxy_eq : c x = c y) : (σ.erase x).image c = σ.image c ∧ (σ.erase y).image c = σ.image c
```

## Dependencies

- Profile.ext
- IsPositiveAffineOf.symm
- Indifferent.symm
