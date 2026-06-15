---
id: isCell-of-door
title: isCell_of_door
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - isCell_of_door
uses:
  - isCell
  - Dominant_of_subset
  - Dominant_of_supset
---

# isCell_of_door

## Lean type

```lean
lemma isCell_of_door (h1 : isDoorof τ D σ C) : IST.isCell τ D
```

## Dependencies

- isCell
- Dominant_of_subset
- Dominant_of_supset
