---
id: SatisfiesNullPlayer
title: SatisfiesNullPlayer
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.CoalitionalGame.ShapleyValue
  declarations:
    - SatisfiesNullPlayer
uses:
  - IsNullPlayer
---

# SatisfiesNullPlayer

## Lean type

```lean
def SatisfiesNullPlayer (φ : CoalitionalGame N ℝ → N → ℝ) : Prop
```

## Dependencies

- IsNullPlayer
