---
id: NC-or-C-of-door
title: NC_or_C_of_door
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - NC_or_C_of_door
uses:
  - isTypedNC
  - isColorful
  - isCell
  - isRoom
  - isRoom_of_Door
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# NC_or_C_of_door

## Lean type

```lean
lemma NC_or_C_of_door (h1 : isTypedNC c i τ D) (h2 : isDoorof τ D σ C) : isTypedNC c i σ C ∨ isColorful c σ C
```

## Dependencies

- isTypedNC
- isColorful
- isCell
- isRoom
- isRoom_of_Door
- IsPositiveAffineOf.symm
- Indifferent.symm
