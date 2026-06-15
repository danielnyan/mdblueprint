---
id: dbcount-NCroom
title: dbcount_NCroom
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - dbcount_NCroom
uses:
  - isColorful
  - isRoom
  - isTypedNC
  - isRoom_of_Door
  - NC_of_NCdoor
  - firber2_doors_NCroom
  - not_colorful_of_TypedNC
---

# dbcount_NCroom

## Lean type

```lean
lemma dbcount_NCroom (i : I) : Even (filter (fun x => ¬isColorful c x.2.1 x.2.2) (dbcountingset c i)).card
```

## Dependencies

- isColorful
- isRoom
- isTypedNC
- isRoom_of_Door
- NC_of_NCdoor
- firber2_doors_NCroom
- not_colorful_of_TypedNC
