---
id: NCtype-of-door
title: NCtype_of_door
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - NCtype_of_door
uses:
  - isTypedNC
---

# NCtype_of_door

## Lean type

```lean
lemma NCtype_of_door (h1 : isTypedNC c i τ D) (_ : isDoorof τ D σ C) (_ : isTypedNC c i σ C) : isTypedNC c i τ D
```

## Dependencies

- isTypedNC
