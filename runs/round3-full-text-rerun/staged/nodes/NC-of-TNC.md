---
id: NC-of-TNC
title: NC_of_TNC
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - NC_of_TNC
uses:
  - isTypedNC
  - isNearlyColorful
---

# NC_of_TNC

## Lean type

```lean
lemma NC_of_TNC (h1 : isTypedNC c i σ C) : isNearlyColorful c σ C
```

## Dependencies

- isTypedNC
- isNearlyColorful
