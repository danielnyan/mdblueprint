---
id: typed-colorful-room-odd
title: typed_colorful_room_odd
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - typed_colorful_room_odd
uses:
  - isColorful
  - _root_.Finset.card_filter_filter_neg
  - isOutsideDoor
  - parity_lemma
  - dbcount_outside_door_odd
  - dbcount_internal_door_even
  - dbcount_NCroom
---

# typed_colorful_room_odd

## Lean type

```lean
lemma typed_colorful_room_odd (i : I): Odd (Finset.filter (fun (x: (Finset T× Finset I) × Finset T × Finset I) => isColorful c x.2.1 x.2.2) (dbcountingset c i)).card
```

## Dependencies

- isColorful
- _root_.Finset.card_filter_filter_neg
- isOutsideDoor
- parity_lemma
- dbcount_outside_door_odd
- dbcount_internal_door_even
- dbcount_NCroom
