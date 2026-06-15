---
id: dbcount-internal-door-even
title: dbcount_internal_door_even
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - dbcount_internal_door_even
uses:
  - isOutsideDoor
  - isInternalDoor
  - isTypedNC
  - fiber_size_internal_door
---

# dbcount_internal_door_even

## Lean type

```lean
lemma dbcount_internal_door_even (i : I) : Even (filter (fun x => ¬ isOutsideDoor x.1.1 x.1.2) (dbcountingset c i)).card
```

## Dependencies

- isOutsideDoor
- isInternalDoor
- isTypedNC
- fiber_size_internal_door
