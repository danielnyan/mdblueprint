---
id: doors-of-NCroom
title: doors_of_NCroom
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - doors_of_NCroom
uses:
  - isRoom
  - isNearlyColorful
  - NCdoors
  - card_of_NCcell
  - isCell
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - Profile.ext
  - image_erase_eq_erase_image_of_unique
  - Dominant_of_subset
  - isDominant
  - Dominant_of_supset
  - injOn_sdiff
  - three_collision_card_bound
  - collision_door_valid
  - image_erase_collision_preserves
  - Transitivity
---

# doors_of_NCroom

## Lean type

```lean
lemma doors_of_NCroom [DecidableEq T] (h_room : isRoom σ C) (h_nc : isNearlyColorful c σ C) : ∃ door1 door2, door1 ≠ door2 ∧ NCdoors c σ C = {door1, door2}
```

## Dependencies

- isRoom
- isNearlyColorful
- NCdoors
- card_of_NCcell
- isCell
- IsPositiveAffineOf.symm
- Indifferent.symm
- Profile.ext
- image_erase_eq_erase_image_of_unique
- Dominant_of_subset
- isDominant
- Dominant_of_supset
- injOn_sdiff
- three_collision_card_bound
- collision_door_valid
- image_erase_collision_preserves
- Transitivity
