---
id: room-of-colorful
title: room_of_colorful
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - room_of_colorful
uses:
  - isColorful
  - isRoom
  - card_le_of_domiant
---

# room_of_colorful

## Lean type

```lean
lemma room_of_colorful (h : IST.isColorful c σ C) : IST.isRoom σ C
```

## Dependencies

- isColorful
- isRoom
- card_le_of_domiant
