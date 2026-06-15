---
id: isRoom-of-Door
title: isRoom_of_Door
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - isRoom_of_Door
uses:
  - isRoom
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# isRoom_of_Door

## Lean type

```lean
lemma isRoom_of_Door (h1 : isDoorof τ D σ C) : IST.isRoom σ C
```

## Dependencies

- isRoom
- IsPositiveAffineOf.symm
- Indifferent.symm
