---
id: card-of-NCcell
title: card_of_NCcell
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - card_of_NCcell
uses:
  - isNearlyColorful
  - card_le_of_domiant
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# card_of_NCcell

## Lean type

```lean
lemma card_of_NCcell (h : isNearlyColorful c σ D) : #σ = #(image c σ) ∨ #σ = #(image c σ) + 1
```

## Dependencies

- isNearlyColorful
- card_le_of_domiant
- IsPositiveAffineOf.symm
- Indifferent.symm
