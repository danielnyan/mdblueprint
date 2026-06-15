---
id: sigma-nonempty-of-room
title: sigma_nonempty_of_room
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - sigma_nonempty_of_room
uses:
  - isRoom
  - Nonempty_of_Dominant
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# sigma_nonempty_of_room

## Lean type

```lean
lemma sigma_nonempty_of_room {σ : Finset T} {C : Finset I} (h : isRoom σ C) : σ.Nonempty
```

## Dependencies

- isRoom
- Nonempty_of_Dominant
- IsPositiveAffineOf.symm
- Indifferent.symm
