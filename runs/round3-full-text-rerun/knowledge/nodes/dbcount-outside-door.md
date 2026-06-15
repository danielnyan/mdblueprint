---
id: dbcount-outside-door
title: dbcount_outside_door
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - dbcount_outside_door
uses:
  - isOutsideDoor
  - outsidedoor_singleton
  - isTypedNC
  - NC_of_outsidedoor
  - Profile.ext
  - outsidedoor_is_singleton
  - isRoom
  - isRoom_of_Door
  - sigma_nonempty_of_room
---

# dbcount_outside_door

## Lean type

```lean
lemma dbcount_outside_door' (i : I): ∃ x, filter (fun x => isOutsideDoor x.1.1 x.1.2) (dbcountingset c i) = {x}
```

## Dependencies

- isOutsideDoor
- outsidedoor_singleton
- isTypedNC
- NC_of_outsidedoor
- Profile.ext
- outsidedoor_is_singleton
- isRoom
- isRoom_of_Door
- sigma_nonempty_of_room
