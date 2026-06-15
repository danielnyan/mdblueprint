---
id: not-colorful-of-TypedNC
title: not_colorful_of_TypedNC
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - not_colorful_of_TypedNC
uses:
  - isTypedNC
  - isColorful
---

# not_colorful_of_TypedNC

## Lean type

```lean
lemma not_colorful_of_TypedNC (h1 : isTypedNC c i σ C) : ¬ IST.isColorful c σ C
```

## Dependencies

- isTypedNC
- isColorful
