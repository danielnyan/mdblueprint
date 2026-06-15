---
id: image-erase-eq-erase-image-of-unique
title: image_erase_eq_erase_image_of_unique
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - image_erase_eq_erase_image_of_unique
uses:
  - Profile.ext
---

# image_erase_eq_erase_image_of_unique

## Lean type

```lean
lemma image_erase_eq_erase_image_of_unique (σ : Finset T) (c : T → I) {z : T} (_ : z ∈ σ) (uniq : ∀ ⦃w⦄, w ∈ σ → c w = c z → w = z) : (σ.erase z).image c = (σ.image c).erase (c z)
```

## Dependencies

- Profile.ext
