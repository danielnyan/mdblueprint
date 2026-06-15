---
id: SatisfiesSymmetry
title: SatisfiesSymmetry
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.CoalitionalGame.ShapleyValue
  declarations:
    - SatisfiesSymmetry
uses:
  - AreSymmetric
---

# SatisfiesSymmetry

## Lean type

```lean
def SatisfiesSymmetry (φ : CoalitionalGame N ℝ → N → ℝ) : Prop
```

## Dependencies

- AreSymmetric
