---
id: outsidedoor-singleton
title: outsidedoor_singleton
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - outsidedoor_singleton
uses:
  - isOutsideDoor
  - isDoor
  - isCell
  - isDominant
---

# outsidedoor_singleton

## Lean type

```lean
lemma outsidedoor_singleton (i : I) : IST.isOutsideDoor Finset.empty {i}
```

## Dependencies

- isOutsideDoor
- isDoor
- isCell
- isDominant
