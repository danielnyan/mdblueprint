---
id: fiber-size-internal-door
title: fiber_size_internal_door
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - fiber_size_internal_door
uses:
  - isInternalDoor
  - isTypedNC
  - isOutsideDoor
  - internal_door_two_rooms
  - Profile.ext
  - isRoom
  - isRoom_of_Door
  - IsPositiveAffineOf.trans
  - StrictlyPreferred.trans
  - Arena.Reachable.trans
  - Indifferent.trans
  - Subtree.trans
---

# fiber_size_internal_door

## Lean type

```lean
lemma fiber_size_internal_door (c : T → I) (i : I) (y : Finset T × Finset I) (hy_internal : IST.isInternalDoor y.1 y.2) (hy_typed : isTypedNC c i y.1 y.2) : let s
```

## Dependencies

- isInternalDoor
- isTypedNC
- isOutsideDoor
- internal_door_two_rooms
- Profile.ext
- isRoom
- isRoom_of_Door
- IsPositiveAffineOf.trans
- StrictlyPreferred.trans
- Arena.Reachable.trans
- Indifferent.trans
- Subtree.trans
