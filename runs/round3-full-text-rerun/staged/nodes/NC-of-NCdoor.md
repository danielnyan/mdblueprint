---
id: NC-of-NCdoor
title: NC_of_NCdoor
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - NC_of_NCdoor
uses:
  - isTypedNC
  - isColorful
  - NC_or_C_of_door
---

# NC_of_NCdoor

## Lean type

```lean
lemma NC_of_NCdoor (h1 : isTypedNC c i τ D) (h2 : isDoorof τ D σ C) : ¬ isColorful c σ C → isTypedNC c i σ C
```

## Dependencies

- isTypedNC
- isColorful
- NC_or_C_of_door
