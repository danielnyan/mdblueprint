---
id: fmA
title: fmA
kind: theorem
status: staged
lean:
  module: EconCSLib.Math.LinearAlgebra.FourierMotzkin
  declarations:
    - fmA
uses:
  - FMRowIndex
---

# fmA

## Lean type

```lean
def fmA (A : I → Fin (n+1) → 𝕜) (idx : FMRowIndex A) (j : Fin n) : 𝕜
```

## Dependencies

- FMRowIndex
