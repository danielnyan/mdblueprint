---
id: Dominant-of-supset
title: Dominant_of_supset
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - Dominant_of_supset
uses:
  - isDominant
---

# Dominant_of_supset

## Lean type

```lean
lemma Dominant_of_supset (σ : Finset T) (C D: Finset I) : C ⊆ D → isDominant σ C → isDominant σ D
```

## Dependencies

- isDominant
