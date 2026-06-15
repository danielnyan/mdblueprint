---
id: NC-of-outsidedoor
title: NC_of_outsidedoor
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - NC_of_outsidedoor
uses:
  - isOutsideDoor
  - isNearlyColorful
  - isCell
  - isDoor
---

# NC_of_outsidedoor

## Lean type

```lean
lemma NC_of_outsidedoor (h : isOutsideDoor σ C) : isNearlyColorful c σ C
```

## Dependencies

- isOutsideDoor
- isNearlyColorful
- isCell
- isDoor
