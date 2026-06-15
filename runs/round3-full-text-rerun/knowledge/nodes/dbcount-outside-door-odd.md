---
id: dbcount-outside-door-odd
title: dbcount_outside_door_odd
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - dbcount_outside_door_odd
uses:
  - isOutsideDoor
  - dbcount_outside_door
---

# dbcount_outside_door_odd

## Lean type

```lean
lemma dbcount_outside_door_odd (i : I): Odd (filter (fun x => isOutsideDoor x.1.1 x.1.2) (dbcountingset c i)).card
```

## Dependencies

- isOutsideDoor
- dbcount_outside_door
