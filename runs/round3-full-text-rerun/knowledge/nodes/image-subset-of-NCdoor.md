---
id: image-subset-of-NCdoor
title: image_subset_of_NCdoor
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - image_subset_of_NCdoor
uses:
  - isNearlyColorful
  - isDoor
  - card_le_of_domiant
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# image_subset_of_NCdoor

## Lean type

```lean
lemma image_subset_of_NCdoor (h1 : isNearlyColorful c σ C) (h2 : isDoor σ C) : image c σ ⊆ C
```

## Dependencies

- isNearlyColorful
- isDoor
- card_le_of_domiant
- IsPositiveAffineOf.symm
- Indifferent.symm
