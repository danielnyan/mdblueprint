---
id: Dominant-of-subset
title: Dominant_of_subset
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.FixedPoint.Scarf
  declarations:
    - Dominant_of_subset
uses:
  - isDominant
---

# Dominant_of_subset

## Lean type

```lean
lemma Dominant_of_subset (σ τ : Finset T) (C : Finset I) : τ ⊆ σ → isDominant σ C → isDominant τ C
```

## Dependencies

- isDominant
