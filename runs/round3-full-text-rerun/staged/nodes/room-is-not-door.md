---
id: room-is-not-door
title: room_is_not_door
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - room_is_not_door
uses:
  - isRoom
  - isDoor
---

# room_is_not_door

## Lean type

```lean
lemma room_is_not_door (h1 : IST.isRoom σ C) : ∀ τ D, ¬ (isDoorof σ C τ D)
```

## Dependencies

- isRoom
- isDoor
