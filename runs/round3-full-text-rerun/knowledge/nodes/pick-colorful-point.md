---
id: pick-colorful-point
title: pick_colorful_point
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - pick_colorful_point
uses:
  - isColorful
  - sigma_nonempty_of_room
  - room_of_colorful
---

# pick_colorful_point

## Lean type

```lean
def pick_colorful_point (h : IST.isColorful c σ C): σ
```

## Dependencies

- isColorful
- sigma_nonempty_of_room
- room_of_colorful
