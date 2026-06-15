---
id: firber2-doors-NCroom
title: firber2_doors_NCroom
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - firber2_doors_NCroom
uses:
  - isRoom
  - isTypedNC
  - doors_of_NCroom
  - NC_of_TNC
  - Profile.ext
  - NCdoors
  - isTypedNC_of_isNearlyColorful_of_isDoorof_isTypedNC
---

# firber2_doors_NCroom

## Lean type

```lean
lemma firber2_doors_NCroom (h0 : isRoom σ C) (h1 : isTypedNC c i σ C) : (filter (fun (x : (Finset T× Finset I)× Finset T × Finset I) => x.2 = (σ,C)) (dbcountingset c i)).card = 2
```

## Dependencies

- isRoom
- isTypedNC
- doors_of_NCroom
- NC_of_TNC
- Profile.ext
- NCdoors
- isTypedNC_of_isNearlyColorful_of_isDoorof_isTypedNC
